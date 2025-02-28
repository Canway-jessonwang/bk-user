<!--
  - Tencent is pleased to support the open source community by making Bk-User 蓝鲸用户管理 available.
  - Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
  - BK-LOG 蓝鲸日志平台 is licensed under the MIT License.
  -
  - License for Bk-User 蓝鲸用户管理:
  - -------------------------------------------------------------------
  -
  - Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
  - documentation files (the "Software"), to deal in the Software without restriction, including without limitation
  - the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
  - and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
  - The above copyright notice and this permission notice shall be included in all copies or substantial
  - portions of the Software.
  -
  - THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
  - LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
  - NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
  - WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  - SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
  -->
<template>
  <div class="table-list-wrapper">
    <div class="thead-container table-container" data-test-id="list_activeTableHeardData">
      <table>
        <thead>
          <tr v-if="userMessage.tableHeardList.length">
            <th v-if="currentCategoryType === 'local' && noSearchOrSearchDepartment" class="checkbox-table-item">
              <label class="king-checkbox king-checkbox-small" @click.stop="selectAll">
                <input type="checkbox" name="checkbox1" :checked="isAllChecked">
              </label>
            </th>
            <th v-for="(heardItem, heardIndex) in activeTableHeardList" :key="heardIndex">
              <span>{{heardItem.name}}</span>
            </th>
          </tr>
        </thead>
      </table>
    </div>
    <div
      class="tbody-container table-container" ref="scrollWrapper"
      @scroll.passive="handleTableScroll" data-test-id="list_organizationData">
      <table v-if="!isEmptySearch">
        <tbody v-if="userMessage.userInforList.length">
          <tr v-for="(item, index) in dataList" :key="item.id + Date.now()" @click.stop="viewDetails(item)">
            <td v-if="currentCategoryType === 'local' && noSearchOrSearchDepartment" class="checkbox-table-item">
              <label class="king-checkbox king-checkbox-small" @click.stop="selectItemInfor(item)">
                <input type="checkbox" name="checkbox1" :checked="item.isCheck">
              </label>
            </td>
            <td
              :class="{ 'hidden': labelName.indexOf(key) !== -1 }"
              v-for="(key, keyIndex) in Object.keys(item)"
              :key="keyIndex">
              <!-- 组织 -->
              <div v-if="key === 'department_name'" class="king-tooltips">
                <span
                  class="staff-text" v-bk-tooltips="{
                    allowHtml: true,
                    content: '#' + key + keyIndex + index,
                    distance: 12,
                    theme: 'light',
                    placement: 'bottom-start'
                  }">{{departmentShift(item[key])}}</span>
                <div :id="key + keyIndex + index">
                  <div v-for="(deItem, deIndex) in item[key]" :key="deIndex">
                    {{deItem}}
                  </div>
                </div>
              </div>
              <!-- 上级 -->
              <div class="list-wrapper" v-else-if="key === 'leader'">
                <span v-bk-overflow-tips>{{getLeaderString(item[key]) || '--'}}</span>
              </div>
              <!-- 其他字段 -->
              <div class="list-wrapper" v-else>
                <span v-bk-overflow-tips>{{getValueByType(key, item[key]) || '--'}}</span>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <div class="empty-search-container" v-else>
        <div class="empty-search">
          <img src="../../../images/svg/info.svg" alt="info">
          <p>{{$t('未找到相符的组织成员')}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    fieldsList: {
      type: Array,
      required: true,
    },
    userMessage: {
      type: Object,
      default: {},
    },
    isEmptySearch: {
      type: Boolean,
      default: false,
    },
    // 控制设置所在组织、批量删除的显示
    isClick: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: true,
    },
    currentCategoryType: {
      type: String,
      default: '',
    },
    noSearchOrSearchDepartment: {
      type: Boolean,
      default: true,
    },
    statusMap: {
      type: Object,
      default: {},
    },
  },
  data() {
    return {
      isAllChecked: false,
      dataList: [], // 展示的列表数据
      dataListPaged: [], // 将列表数据按 pageSize 分页
      throttle: false, // 滚动节流 是否进入cd
      isPageOver: false, // 前端分页加载是否结束
      count: null, // 数据总条数
      pageSize: null, // 每页展示多少数据
      totalPage: null, // 计算出总共多少页
      currentPage: null, // 当前加载了多少页
      pageLimit: 20, // 大于此条数前端分页
      lineHeight: 42, // 列表行高
      labelName: ['id', 'isCheck', 'departments', 'originItem', 'create_time', 'update_time'],
    };
  },
  computed: {
    activeTableHeardList() {
      const arr = ['id', 'isCheck', 'departments', 'create_time', 'update_time'];
      return this.userMessage.tableHeardList.filter(item => arr.indexOf(item.key) === -1);
    },
    enumInfo() {
      const enumInfo = {};
      const fieldsList = JSON.parse(JSON.stringify(this.fieldsList));
      fieldsList.forEach((fieldInfo) => {
        if (fieldInfo.type === 'one_enum') {
          enumInfo[fieldInfo.key] = {
            type: 'one_enum',
            options: fieldInfo.options,
          };
        } else if (fieldInfo.type === 'multi_enum') {
          enumInfo[fieldInfo.key] = {
            type: 'multi_enum',
            options: fieldInfo.options,
          };
        }
      });
      return enumInfo;
    },
  },
  watch: {
    'userMessage.userInforList'(value) {
      this.handleOriginList(value);
    },
    activeTableHeardList: {
      immediate: true,
      handler(value) {
        this.$emit('updateHeardList', value);
      },
    },
  },
  mounted() {
    if (this.userMessage.userInforList && this.userMessage.userInforList.length) {
      this.handleOriginList(this.userMessage.userInforList);
    }
  },
  methods: {
    handleOriginList(value) {
      this.$emit('updateTableData', value);
      if (this.isAllChecked) {
        this.isAllChecked = false;
      }
      this.$refs.scrollWrapper.scrollTo({ top: 0 });

      if (value.length > this.pageLimit) {
        this.dataList = [];
        this.initPageConf(value);
        this.loadPage();
      } else {
        this.dataList = value;
        this.isPageOver = true;
      }
    },
    initPageConf(list) {
      this.currentPage = 0;
      this.isPageOver = false;

      this.count = list.length;
      this.pageSize = Math.ceil(this.$refs.scrollWrapper.offsetHeight / this.lineHeight);
      this.totalPage = Math.ceil(this.count / this.pageSize) || 1;

      this.dataListShadow = [...list];
      this.dataListPaged = [];
      for (let i = 0; i < this.count; i += this.pageSize) {
        this.dataListPaged.push(this.dataListShadow.slice(i, i + this.pageSize));
      }
    },
    loadPage() {
      this.currentPage += 1;
      this.isPageOver = this.currentPage === this.totalPage;
      this.dataList.splice(this.dataList.length, 0, ...this.dataListPaged[this.currentPage - 1]);
    },
    handleTableScroll(e) {
      if (this.isPageOver || this.throttle) {
        return;
      }

      this.throttle = true;
      setTimeout(() => {
        this.throttle = false;
        if (e.target.scrollHeight - e.target.offsetHeight - e.target.scrollTop < 10) {
          this.loadPage();
        }
      }, 200);
    },
    departmentShift(departList) {
      let result = '';
      departList.forEach((item) => {
        const itemArr = item.split('/');
        result += `${itemArr[itemArr.length - 1]}/`;
      });
      return result.slice(0, result.length - 1).split('/')
        .join(';');
    },
    getLeaderString(leader) {
      return leader && leader.map((item) => {
        return item.username;
      }).join(';');
    },
    getValueByType(key, value) {
      if (this.enumInfo[key]) {
        // 枚举值
        const options = this.enumInfo[key].options;
        if (this.enumInfo[key].type === 'one_enum') {
          // 单选 value 期望是数值或字符串
          if (typeof value !== 'number' && typeof value !== 'string') {
            console.warn(`${key} ${this.$t('字段的值应该是数值或字符串')}（options.id）`);
            return '';
          }
          for (let i = 0; i < options.length; i++) {
            if (options[i].id === value) {
              if (this.$i18n.locale === 'en') {
                return value;
              }
              return this.statusMap[options[i].id];
            }
          }
        } else {
          // 多选 value 期望是数组
          if (!Array.isArray(value)) {
            console.warn(`${key} ${this.$t('字段的值应该是数组')}`);
            return '';
          }
          const results = [];
          value.forEach((item) => {
            for (let i = 0; i < options.length; i++) {
              if (options[i].id === item) {
                results.push(options[i].value);
                break;
              }
            }
          });
          return results.join(';');
        }
      } else {
        return value;
      }
    },
    // 单选、多选
    selectItemInfor(item) {
      item.isCheck = !item.isCheck;
      this.isAllChecked = !this.userMessage.userInforList.some((element) => {
        return !element.isCheck;
      });
      const isClick = this.userMessage.userInforList.some((element) => {
        return element.isCheck;
      });
      this.$emit('update:isClick', isClick);
    },
    // 点击查看当前用户的信息： 1.调用接口，拿到当前用户的信息 成功后抛给父组件
    viewDetails(item) {
      this.$emit('viewDetails', item.originItem);
    },
    // 全选
    selectAll() {
      this.isAllChecked = !this.isAllChecked;
      this.userMessage.userInforList.forEach((item) => {
        item.isCheck = this.isAllChecked;
      });
      this.$emit('update:isClick', this.isAllChecked);
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../../../scss/mixins/scroller';

.table-list-wrapper {
  margin-bottom: 20px;
  height: calc(100% - 66px);
  border: 1px solid #dcdee5;

  > .table-container {
    // table 公用样式
    > table {
      width: 100%;
      table-layout: fixed;
      border: none;
      border-collapse: collapse;
      font-size: 12px;

      tr {
        height: 42px;
        border-bottom: 1px solid #dcdee5;
      }

      .king-checkbox {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 20px;
        margin-right: 0;
        padding: 0;

        input {
          margin: 0;
        }
      }
    }
  }

  > .thead-container {
    height: 42px;

    > table {
      background: #fafbfd;

      th {
        padding: 0 10px;
        text-align: left;
        border: none;
        cursor: text;
        color: #666;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        // checkbox
        &.checkbox-table-item {
          width: 60px;
          text-align: center;
        }

        &.hidden {
          display: none;
        }

        > span {
          font-size: 12px;
          height: 20px;
          line-height: 20px;
        }
      }
    }
  }

  > .tbody-container {
    height: calc(100% - 42px);
    overflow: hidden auto;

    @include scroller($backgroundColor: #e6e9ea, $width: 4px);

    > table > tbody > tr {
      cursor: pointer;
      transition: all .3s ease;

      &:hover {
        background: #e1ecff;
      }

      > td {
        padding: 0 10px;
        border: none;
        // checkbox
        &.checkbox-table-item {
          width: 60px;
          text-align: center;
        }

        &.hidden {
          display: none;
        }

        > .list-wrapper {
          width: 100%;

          span {
            display: block;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
          }
        }

        > div {
          height: 20px;
          line-height: 20px;
        }

        .king-tooltips {
          .staff-text {
            width: 100%;
            outline: none;
            display: inline-block;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
          }
        }
      }
    }
  }
}

.empty-search-container {
  position: relative;
  width: 100%;
  height: 100%;
  border-top: 1px solid #dcdee5;

  .empty-search {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-flow: column;
    height: 80%;

    img {
      width: 42px;
      margin-bottom: 10px;
    }

    p {
      height: 19px;
      font-size: 14px;
      font-weight: bold;
      color: #63656e;
      line-height: 19px;
    }
  }
}
</style>

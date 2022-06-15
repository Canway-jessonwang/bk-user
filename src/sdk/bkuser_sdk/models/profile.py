# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from bkuser_sdk.models.leader import Leader  # noqa: F401,E501
from bkuser_sdk.models.simple_department import SimpleDepartment  # noqa: F401,E501


class Profile(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'username': 'str',
        'password_valid_days': 'int',
        'departments': 'list[SimpleDepartment]',
        'extras': 'object',
        'leader': 'list[Leader]',
        'last_login_time': 'datetime',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'qq': 'str',
        'email': 'str',
        'telephone': 'str',
        'wx_userid': 'str',
        'wx_openid': 'str',
        'code': 'str',
        'domain': 'str',
        'category_id': 'int',
        'display_name': 'str',
        'logo': 'str',
        'status': 'str',
        'staff_status': 'str',
        'password_update_time': 'datetime',
        'position': 'int',
        'account_expiration_date': 'date',
        'time_zone': 'str',
        'language': 'str',
        'country_code': 'str',
        'iso_code': 'str',
        'enabled': 'bool',
        'type': 'str',
        'role': 'int'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'password_valid_days': 'password_valid_days',
        'departments': 'departments',
        'extras': 'extras',
        'leader': 'leader',
        'last_login_time': 'last_login_time',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'qq': 'qq',
        'email': 'email',
        'telephone': 'telephone',
        'wx_userid': 'wx_userid',
        'wx_openid': 'wx_openid',
        'code': 'code',
        'domain': 'domain',
        'category_id': 'category_id',
        'display_name': 'display_name',
        'logo': 'logo',
        'status': 'status',
        'staff_status': 'staff_status',
        'password_update_time': 'password_update_time',
        'position': 'position',
        'account_expiration_date': 'account_expiration_date',
        'time_zone': 'time_zone',
        'language': 'language',
        'country_code': 'country_code',
        'iso_code': 'iso_code',
        'enabled': 'enabled',
        'type': 'type',
        'role': 'role'
    }

    def __init__(self, id=None, username=None, password_valid_days=None, departments=None, extras=None, leader=None, last_login_time=None, create_time=None, update_time=None, qq=None, email=None, telephone=None, wx_userid=None, wx_openid=None, code=None, domain=None, category_id=None, display_name=None, logo=None, status=None, staff_status=None, password_update_time=None, position=None, account_expiration_date=None, time_zone=None, language=None, country_code=None, iso_code=None, enabled=None, type=None, role=None):  # noqa: E501
        """Profile - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._password_valid_days = None
        self._departments = None
        self._extras = None
        self._leader = None
        self._last_login_time = None
        self._create_time = None
        self._update_time = None
        self._qq = None
        self._email = None
        self._telephone = None
        self._wx_userid = None
        self._wx_openid = None
        self._code = None
        self._domain = None
        self._category_id = None
        self._display_name = None
        self._logo = None
        self._status = None
        self._staff_status = None
        self._password_update_time = None
        self._position = None
        self._account_expiration_date = None
        self._time_zone = None
        self._language = None
        self._country_code = None
        self._iso_code = None
        self._enabled = None
        self._type = None
        self._role = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if password_valid_days is not None:
            self.password_valid_days = password_valid_days
        if departments is not None:
            self.departments = departments
        if extras is not None:
            self.extras = extras
        if leader is not None:
            self.leader = leader
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if qq is not None:
            self.qq = qq
        if email is not None:
            self.email = email
        if telephone is not None:
            self.telephone = telephone
        if wx_userid is not None:
            self.wx_userid = wx_userid
        if wx_openid is not None:
            self.wx_openid = wx_openid
        if code is not None:
            self.code = code
        if domain is not None:
            self.domain = domain
        self.category_id = category_id
        if display_name is not None:
            self.display_name = display_name
        if logo is not None:
            self.logo = logo
        if status is not None:
            self.status = status
        if staff_status is not None:
            self.staff_status = staff_status
        if password_update_time is not None:
            self.password_update_time = password_update_time
        if position is not None:
            self.position = position
        if account_expiration_date is not None:
            self.account_expiration_date = account_expiration_date
        if time_zone is not None:
            self.time_zone = time_zone
        if language is not None:
            self.language = language
        if country_code is not None:
            self.country_code = country_code
        if iso_code is not None:
            self.iso_code = iso_code
        if enabled is not None:
            self.enabled = enabled
        if type is not None:
            self.type = type
        if role is not None:
            self.role = role

    @property
    def id(self):
        """Gets the id of this Profile.  # noqa: E501


        :return: The id of this Profile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Profile.


        :param id: The id of this Profile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this Profile.  # noqa: E501


        :return: The username of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Profile.


        :param username: The username of this Profile.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password_valid_days(self):
        """Gets the password_valid_days of this Profile.  # noqa: E501


        :return: The password_valid_days of this Profile.  # noqa: E501
        :rtype: int
        """
        return self._password_valid_days

    @password_valid_days.setter
    def password_valid_days(self, password_valid_days):
        """Sets the password_valid_days of this Profile.


        :param password_valid_days: The password_valid_days of this Profile.  # noqa: E501
        :type: int
        """

        self._password_valid_days = password_valid_days

    @property
    def departments(self):
        """Gets the departments of this Profile.  # noqa: E501


        :return: The departments of this Profile.  # noqa: E501
        :rtype: list[SimpleDepartment]
        """
        return self._departments

    @departments.setter
    def departments(self, departments):
        """Sets the departments of this Profile.


        :param departments: The departments of this Profile.  # noqa: E501
        :type: list[SimpleDepartment]
        """

        self._departments = departments

    @property
    def extras(self):
        """Gets the extras of this Profile.  # noqa: E501


        :return: The extras of this Profile.  # noqa: E501
        :rtype: object
        """
        return self._extras

    @extras.setter
    def extras(self, extras):
        """Sets the extras of this Profile.


        :param extras: The extras of this Profile.  # noqa: E501
        :type: object
        """

        self._extras = extras

    @property
    def leader(self):
        """Gets the leader of this Profile.  # noqa: E501


        :return: The leader of this Profile.  # noqa: E501
        :rtype: list[Leader]
        """
        return self._leader

    @leader.setter
    def leader(self, leader):
        """Sets the leader of this Profile.


        :param leader: The leader of this Profile.  # noqa: E501
        :type: list[Leader]
        """

        self._leader = leader

    @property
    def last_login_time(self):
        """Gets the last_login_time of this Profile.  # noqa: E501


        :return: The last_login_time of this Profile.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this Profile.


        :param last_login_time: The last_login_time of this Profile.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def create_time(self):
        """Gets the create_time of this Profile.  # noqa: E501


        :return: The create_time of this Profile.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Profile.


        :param create_time: The create_time of this Profile.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Profile.  # noqa: E501


        :return: The update_time of this Profile.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Profile.


        :param update_time: The update_time of this Profile.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def qq(self):
        """Gets the qq of this Profile.  # noqa: E501


        :return: The qq of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._qq

    @qq.setter
    def qq(self, qq):
        """Sets the qq of this Profile.


        :param qq: The qq of this Profile.  # noqa: E501
        :type: str
        """

        self._qq = qq

    @property
    def email(self):
        """Gets the email of this Profile.  # noqa: E501


        :return: The email of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Profile.


        :param email: The email of this Profile.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def telephone(self):
        """Gets the telephone of this Profile.  # noqa: E501


        :return: The telephone of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this Profile.


        :param telephone: The telephone of this Profile.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

    @property
    def wx_userid(self):
        """Gets the wx_userid of this Profile.  # noqa: E501


        :return: The wx_userid of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._wx_userid

    @wx_userid.setter
    def wx_userid(self, wx_userid):
        """Sets the wx_userid of this Profile.


        :param wx_userid: The wx_userid of this Profile.  # noqa: E501
        :type: str
        """

        self._wx_userid = wx_userid

    @property
    def wx_openid(self):
        """Gets the wx_openid of this Profile.  # noqa: E501


        :return: The wx_openid of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._wx_openid

    @wx_openid.setter
    def wx_openid(self, wx_openid):
        """Sets the wx_openid of this Profile.


        :param wx_openid: The wx_openid of this Profile.  # noqa: E501
        :type: str
        """

        self._wx_openid = wx_openid

    @property
    def code(self):
        """Gets the code of this Profile.  # noqa: E501


        :return: The code of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Profile.


        :param code: The code of this Profile.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def domain(self):
        """Gets the domain of this Profile.  # noqa: E501


        :return: The domain of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Profile.


        :param domain: The domain of this Profile.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def category_id(self):
        """Gets the category_id of this Profile.  # noqa: E501


        :return: The category_id of this Profile.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this Profile.


        :param category_id: The category_id of this Profile.  # noqa: E501
        :type: int
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def display_name(self):
        """Gets the display_name of this Profile.  # noqa: E501


        :return: The display_name of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Profile.


        :param display_name: The display_name of this Profile.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def logo(self):
        """Gets the logo of this Profile.  # noqa: E501


        :return: The logo of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Profile.


        :param logo: The logo of this Profile.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def status(self):
        """Gets the status of this Profile.  # noqa: E501


        :return: The status of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Profile.


        :param status: The status of this Profile.  # noqa: E501
        :type: str
        """
        allowed_values = ["NORMAL", "LOCKED", "DELETED", "DISABLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def staff_status(self):
        """Gets the staff_status of this Profile.  # noqa: E501


        :return: The staff_status of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._staff_status

    @staff_status.setter
    def staff_status(self, staff_status):
        """Sets the staff_status of this Profile.


        :param staff_status: The staff_status of this Profile.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN", "OUT"]  # noqa: E501
        if staff_status not in allowed_values:
            raise ValueError(
                "Invalid value for `staff_status` ({0}), must be one of {1}"  # noqa: E501
                .format(staff_status, allowed_values)
            )

        self._staff_status = staff_status

    @property
    def password_update_time(self):
        """Gets the password_update_time of this Profile.  # noqa: E501


        :return: The password_update_time of this Profile.  # noqa: E501
        :rtype: datetime
        """
        return self._password_update_time

    @password_update_time.setter
    def password_update_time(self, password_update_time):
        """Sets the password_update_time of this Profile.


        :param password_update_time: The password_update_time of this Profile.  # noqa: E501
        :type: datetime
        """

        self._password_update_time = password_update_time

    @property
    def position(self):
        """Gets the position of this Profile.  # noqa: E501


        :return: The position of this Profile.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Profile.


        :param position: The position of this Profile.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def account_expiration_date(self):
        """Gets the account_expiration_date of this Profile.  # noqa: E501


        :return: The account_expiration_date of this Profile.  # noqa: E501
        :rtype: date
        """
        return self._account_expiration_date

    @account_expiration_date.setter
    def account_expiration_date(self, account_expiration_date):
        """Sets the account_expiration_date of this Profile.


        :param account_expiration_date: The account_expiration_date of this Profile.  # noqa: E501
        :type: date
        """

        self._account_expiration_date = account_expiration_date

    @property
    def time_zone(self):
        """Gets the time_zone of this Profile.  # noqa: E501


        :return: The time_zone of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Profile.


        :param time_zone: The time_zone of this Profile.  # noqa: E501
        :type: str
        """
        allowed_values = ["Africa/Abidjan", "Africa/Accra", "Africa/Addis_Ababa", "Africa/Algiers", "Africa/Asmara", "Africa/Bamako", "Africa/Bangui", "Africa/Banjul", "Africa/Bissau", "Africa/Blantyre", "Africa/Brazzaville", "Africa/Bujumbura", "Africa/Cairo", "Africa/Casablanca", "Africa/Ceuta", "Africa/Conakry", "Africa/Dakar", "Africa/Dar_es_Salaam", "Africa/Djibouti", "Africa/Douala", "Africa/El_Aaiun", "Africa/Freetown", "Africa/Gaborone", "Africa/Harare", "Africa/Johannesburg", "Africa/Juba", "Africa/Kampala", "Africa/Khartoum", "Africa/Kigali", "Africa/Kinshasa", "Africa/Lagos", "Africa/Libreville", "Africa/Lome", "Africa/Luanda", "Africa/Lubumbashi", "Africa/Lusaka", "Africa/Malabo", "Africa/Maputo", "Africa/Maseru", "Africa/Mbabane", "Africa/Mogadishu", "Africa/Monrovia", "Africa/Nairobi", "Africa/Ndjamena", "Africa/Niamey", "Africa/Nouakchott", "Africa/Ouagadougou", "Africa/Porto-Novo", "Africa/Sao_Tome", "Africa/Tripoli", "Africa/Tunis", "Africa/Windhoek", "America/Adak", "America/Anchorage", "America/Anguilla", "America/Antigua", "America/Araguaina", "America/Argentina/Buenos_Aires", "America/Argentina/Catamarca", "America/Argentina/Cordoba", "America/Argentina/Jujuy", "America/Argentina/La_Rioja", "America/Argentina/Mendoza", "America/Argentina/Rio_Gallegos", "America/Argentina/Salta", "America/Argentina/San_Juan", "America/Argentina/San_Luis", "America/Argentina/Tucuman", "America/Argentina/Ushuaia", "America/Aruba", "America/Asuncion", "America/Atikokan", "America/Bahia", "America/Bahia_Banderas", "America/Barbados", "America/Belem", "America/Belize", "America/Blanc-Sablon", "America/Boa_Vista", "America/Bogota", "America/Boise", "America/Cambridge_Bay", "America/Campo_Grande", "America/Cancun", "America/Caracas", "America/Cayenne", "America/Cayman", "America/Chicago", "America/Chihuahua", "America/Costa_Rica", "America/Creston", "America/Cuiaba", "America/Curacao", "America/Danmarkshavn", "America/Dawson", "America/Dawson_Creek", "America/Denver", "America/Detroit", "America/Dominica", "America/Edmonton", "America/Eirunepe", "America/El_Salvador", "America/Fort_Nelson", "America/Fortaleza", "America/Glace_Bay", "America/Goose_Bay", "America/Grand_Turk", "America/Grenada", "America/Guadeloupe", "America/Guatemala", "America/Guayaquil", "America/Guyana", "America/Halifax", "America/Havana", "America/Hermosillo", "America/Indiana/Indianapolis", "America/Indiana/Knox", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Tell_City", "America/Indiana/Vevay", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Inuvik", "America/Iqaluit", "America/Jamaica", "America/Juneau", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/Kralendijk", "America/La_Paz", "America/Lima", "America/Los_Angeles", "America/Lower_Princes", "America/Maceio", "America/Managua", "America/Manaus", "America/Marigot", "America/Martinique", "America/Matamoros", "America/Mazatlan", "America/Menominee", "America/Merida", "America/Metlakatla", "America/Mexico_City", "America/Miquelon", "America/Moncton", "America/Monterrey", "America/Montevideo", "America/Montserrat", "America/Nassau", "America/New_York", "America/Nipigon", "America/Nome", "America/Noronha", "America/North_Dakota/Beulah", "America/North_Dakota/Center", "America/North_Dakota/New_Salem", "America/Nuuk", "America/Ojinaga", "America/Panama", "America/Pangnirtung", "America/Paramaribo", "America/Phoenix", "America/Port-au-Prince", "America/Port_of_Spain", "America/Porto_Velho", "America/Puerto_Rico", "America/Punta_Arenas", "America/Rainy_River", "America/Rankin_Inlet", "America/Recife", "America/Regina", "America/Resolute", "America/Rio_Branco", "America/Santarem", "America/Santiago", "America/Santo_Domingo", "America/Sao_Paulo", "America/Scoresbysund", "America/Sitka", "America/St_Barthelemy", "America/St_Johns", "America/St_Kitts", "America/St_Lucia", "America/St_Thomas", "America/St_Vincent", "America/Swift_Current", "America/Tegucigalpa", "America/Thule", "America/Thunder_Bay", "America/Tijuana", "America/Toronto", "America/Tortola", "America/Vancouver", "America/Whitehorse", "America/Winnipeg", "America/Yakutat", "America/Yellowknife", "Antarctica/Casey", "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Macquarie", "Antarctica/Mawson", "Antarctica/McMurdo", "Antarctica/Palmer", "Antarctica/Rothera", "Antarctica/Syowa", "Antarctica/Troll", "Antarctica/Vostok", "Arctic/Longyearbyen", "Asia/Aden", "Asia/Almaty", "Asia/Amman", "Asia/Anadyr", "Asia/Aqtau", "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Atyrau", "Asia/Baghdad", "Asia/Bahrain", "Asia/Baku", "Asia/Bangkok", "Asia/Barnaul", "Asia/Beirut", "Asia/Bishkek", "Asia/Brunei", "Asia/Chita", "Asia/Choibalsan", "Asia/Colombo", "Asia/Damascus", "Asia/Dhaka", "Asia/Dili", "Asia/Dubai", "Asia/Dushanbe", "Asia/Famagusta", "Asia/Gaza", "Asia/Hebron", "Asia/Ho_Chi_Minh", "Asia/Hong_Kong", "Asia/Hovd", "Asia/Irkutsk", "Asia/Jakarta", "Asia/Jayapura", "Asia/Jerusalem", "Asia/Kabul", "Asia/Kamchatka", "Asia/Karachi", "Asia/Kathmandu", "Asia/Khandyga", "Asia/Kolkata", "Asia/Krasnoyarsk", "Asia/Kuala_Lumpur", "Asia/Kuching", "Asia/Kuwait", "Asia/Macau", "Asia/Magadan", "Asia/Makassar", "Asia/Manila", "Asia/Muscat", "Asia/Nicosia", "Asia/Novokuznetsk", "Asia/Novosibirsk", "Asia/Omsk", "Asia/Oral", "Asia/Phnom_Penh", "Asia/Pontianak", "Asia/Pyongyang", "Asia/Qatar", "Asia/Qostanay", "Asia/Qyzylorda", "Asia/Riyadh", "Asia/Sakhalin", "Asia/Samarkand", "Asia/Seoul", "Asia/Shanghai", "Asia/Singapore", "Asia/Srednekolymsk", "Asia/Taipei", "Asia/Tashkent", "Asia/Tbilisi", "Asia/Tehran", "Asia/Thimphu", "Asia/Tokyo", "Asia/Tomsk", "Asia/Ulaanbaatar", "Asia/Urumqi", "Asia/Ust-Nera", "Asia/Vientiane", "Asia/Vladivostok", "Asia/Yakutsk", "Asia/Yangon", "Asia/Yekaterinburg", "Asia/Yerevan", "Atlantic/Azores", "Atlantic/Bermuda", "Atlantic/Canary", "Atlantic/Cape_Verde", "Atlantic/Faroe", "Atlantic/Madeira", "Atlantic/Reykjavik", "Atlantic/South_Georgia", "Atlantic/St_Helena", "Atlantic/Stanley", "Australia/Adelaide", "Australia/Brisbane", "Australia/Broken_Hill", "Australia/Darwin", "Australia/Eucla", "Australia/Hobart", "Australia/Lindeman", "Australia/Lord_Howe", "Australia/Melbourne", "Australia/Perth", "Australia/Sydney", "Canada/Atlantic", "Canada/Central", "Canada/Eastern", "Canada/Mountain", "Canada/Newfoundland", "Canada/Pacific", "Europe/Amsterdam", "Europe/Andorra", "Europe/Astrakhan", "Europe/Athens", "Europe/Belgrade", "Europe/Berlin", "Europe/Bratislava", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest", "Europe/Busingen", "Europe/Chisinau", "Europe/Copenhagen", "Europe/Dublin", "Europe/Gibraltar", "Europe/Guernsey", "Europe/Helsinki", "Europe/Isle_of_Man", "Europe/Istanbul", "Europe/Jersey", "Europe/Kaliningrad", "Europe/Kiev", "Europe/Kirov", "Europe/Lisbon", "Europe/Ljubljana", "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Mariehamn", "Europe/Minsk", "Europe/Monaco", "Europe/Moscow", "Europe/Oslo", "Europe/Paris", "Europe/Podgorica", "Europe/Prague", "Europe/Riga", "Europe/Rome", "Europe/Samara", "Europe/San_Marino", "Europe/Sarajevo", "Europe/Saratov", "Europe/Simferopol", "Europe/Skopje", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Tirane", "Europe/Ulyanovsk", "Europe/Uzhgorod", "Europe/Vaduz", "Europe/Vatican", "Europe/Vienna", "Europe/Vilnius", "Europe/Volgograd", "Europe/Warsaw", "Europe/Zagreb", "Europe/Zaporozhye", "Europe/Zurich", "GMT", "Indian/Antananarivo", "Indian/Chagos", "Indian/Christmas", "Indian/Cocos", "Indian/Comoro", "Indian/Kerguelen", "Indian/Mahe", "Indian/Maldives", "Indian/Mauritius", "Indian/Mayotte", "Indian/Reunion", "Pacific/Apia", "Pacific/Auckland", "Pacific/Bougainville", "Pacific/Chatham", "Pacific/Chuuk", "Pacific/Easter", "Pacific/Efate", "Pacific/Enderbury", "Pacific/Fakaofo", "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Galapagos", "Pacific/Gambier", "Pacific/Guadalcanal", "Pacific/Guam", "Pacific/Honolulu", "Pacific/Kiritimati", "Pacific/Kosrae", "Pacific/Kwajalein", "Pacific/Majuro", "Pacific/Marquesas", "Pacific/Midway", "Pacific/Nauru", "Pacific/Niue", "Pacific/Norfolk", "Pacific/Noumea", "Pacific/Pago_Pago", "Pacific/Palau", "Pacific/Pitcairn", "Pacific/Pohnpei", "Pacific/Port_Moresby", "Pacific/Rarotonga", "Pacific/Saipan", "Pacific/Tahiti", "Pacific/Tarawa", "Pacific/Tongatapu", "Pacific/Wake", "Pacific/Wallis", "US/Alaska", "US/Arizona", "US/Central", "US/Eastern", "US/Hawaii", "US/Mountain", "US/Pacific", "UTC"]  # noqa: E501
        if time_zone not in allowed_values:
            raise ValueError(
                "Invalid value for `time_zone` ({0}), must be one of {1}"  # noqa: E501
                .format(time_zone, allowed_values)
            )

        self._time_zone = time_zone

    @property
    def language(self):
        """Gets the language of this Profile.  # noqa: E501


        :return: The language of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Profile.


        :param language: The language of this Profile.  # noqa: E501
        :type: str
        """
        allowed_values = ["zh-cn", "en"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def country_code(self):
        """Gets the country_code of this Profile.  # noqa: E501


        :return: The country_code of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Profile.


        :param country_code: The country_code of this Profile.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def iso_code(self):
        """Gets the iso_code of this Profile.  # noqa: E501


        :return: The iso_code of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """Sets the iso_code of this Profile.


        :param iso_code: The iso_code of this Profile.  # noqa: E501
        :type: str
        """

        self._iso_code = iso_code

    @property
    def enabled(self):
        """Gets the enabled of this Profile.  # noqa: E501


        :return: The enabled of this Profile.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Profile.


        :param enabled: The enabled of this Profile.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def type(self):
        """Gets the type of this Profile.  # noqa: E501


        :return: The type of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Profile.


        :param type: The type of this Profile.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def role(self):
        """Gets the role of this Profile.  # noqa: E501


        :return: The role of this Profile.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Profile.


        :param role: The role of this Profile.  # noqa: E501
        :type: int
        """

        self._role = role

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Profile, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Profile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

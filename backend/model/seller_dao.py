import pymysql


class SellerDao:
    def check_existing_product_name(self, product_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT
                    name
                FROM
                    products
                WHERE
                    name = %(product_name)s
                AND
                    seller_id = %(user_id)s
            """
            cursor.execute(query, product_info)
            existing_product_name = cursor.fetchone()
            return existing_product_name

    def create_product(self, product_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO product_logs(
                    product_id,
                    seller_id,
                    product_category_id,
                    name,
                    discount_start,
                    discount_end,
                    discount_rate,
                    price,
                    discountPrice,
                    contents_image,
                    created_at,
                    updated_at,
                    is_selling,
                    code,
                    is_display,
                    is_discount,
                    minimum,
                    maximum
                )
                VALUES(
                    %(user_id)s,
                    %(product_category_id)s,
                    %(product_name)s,
                    %(discount_start)s,
                    %(discount_end)s,
                    %(discount_rate)s,
                    %(price)s,
                    %(discount_price)s,
                    %(product_detail_image)s,
                    NOW(),
                    NOW(),
                    %(is_selling)s,
                    FLOOR(RAND() * 901) + 100,
                    %(is_display)s,
                    %(is_discount)s,
                    %(minimum)s,
                    %(maximum)s,
            """
            cursor.execute(query, product_info)
            new_product_id = cursor.lastrowid
            return new_product_id

    def create_product_log(self, product_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO product_logs(
                    product_id,
                    seller_id,
                    product_category_id,
                    name,
                    discount_start,
                    discount_end,
                    discount_rate,
                    price,
                    discountPrice,
                    contents_image,
                    created_at,
                    updated_at,
                    is_selling,
                    code,
                    is_display,
                    is_discount,
                    minimum,
                    maximum,
                    is_delete,
                    changer_id,
                    change_date
                )
                VALUES(
                    %(product_id)s,
                    %(user_id)s,
                    %(product_category_id)s,
                    %(product_name)s,
                    %(discount_start)s,
                    %(discount_end)s,
                    %(discount_rate)s,
                    %(price)s,
                    %(discount_price)s,
                    %(product_detail_image)s,
                    NOW(),
                    NOW(),
                    %(is_selling)s,
                    FLOOR(RAND() * 901) + 100,
                    %(is_display)s,
                    %(is_discount)s,
                    %(minimum)s,
                    %(maximum)s,
                    0,
                    %(user_id)s,
                    SELECT created_at FROM products WHERE id = %(new_product_id)s
                )
            """
            cursor.execute(query, product_info)
            new_product_log_id = cursor.lastrowid
            return new_product_log_id

    def create_product_option(self, product_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO product_options(
                    product_color_type_id,
                    product_size_type_id,
                    product_id,
                    stock 
                ) 
                VALUES(
                    %(product_color_id)s,
                    %(product_size_id)s,
                    %(product_id)s,
                    %(stock)s
                )
            """
            cursor.execute(query, product_info)
            new_product_option_id = cursor.lastrowid
            return new_product_option_id

    def create_product_option_log(self, product_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO product_option_logs(
                    product_option_id,
                    product_color_type_id,
                    product_size_type_id,
                    product_id,
                    stock,
                    changer_id,
                    change_date 
                ) 
                VALUES(
                    %(product_option_id)s,
                    %(product_color_id)s,
                    %(product_size_id)s,
                    %(product_id)s,
                    %(stock)s,
                    %(user_id)s,
                    NOW()
                )
            """
            cursor.execute(query, product_info)
            product_option_log_id = cursor.lastrowid
            return product_option_log_id

    def create_product_thumbnail(self, product_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO product_thumbnails(
                    product_id,
                    image_url,
                    ordering
                )
                VALUES(
                    %(product_id)s,
                    %(product_thumbnail_image)s,
                    1
                )
            """
            cursor.execute(query, product_info)
            product_thumbnail_id = cursor.lastrowid
            return product_thumbnail_id

    def create_product_thumbnail_log(self, product_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO product_thumbnail_logs(
                    product_thumbnail_id,
                    product_id,
                    image_url,
                    ordering,
                    changer_id,
                    change_date
                )
                VALUES(
                    %(product_thumbnail_id)s,
                    %(product_id)s,
                    %(product_thumbnail_image)s,
                    1,
                    %(user_id)s,
                    NOW()
                )
            """
            cursor.execute(query, product_info)
            product_thumbnail_log_id = cursor.lastrowid
            return product_thumbnail_log_id

    def find_seller_username(self, seller_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            find_seller_info = """
            SELECT
                username 
            FROM
                user_info
            WHERE
                username = %(username)s
            """
            cursor.execute(find_seller_info, seller_info)
            seller_username = cursor.fetchone()
            return seller_username

    def check_seller_korean_brand_name(self, seller_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            check_korean_brand_name = """
            SELECT
                korean_brand_name
            FROM
                sellers
            WHERE
                korean_brand_name = %(korean_brand_name)s
            """

            cursor.execute(check_korean_brand_name, seller_info)
            seller_korean_brand_name = cursor.fetchone()
            return seller_korean_brand_name

    def check_seller_english_brand_name(self, seller_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            check_korean_brand_name = """
            SELECT
                english_brand_name
            FROM
                sellers
            WHERE
                english_brand_name = %(english_brand_name)s
            """

            cursor.execute(check_korean_brand_name, seller_info)
            seller_english_brand_name = cursor.fetchone()
            return seller_english_brand_name

    def create_seller(self, seller_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            create_seller = """
            INSERT INTO sellers(
                user_info_id,
                seller_category_id,
                korean_brand_name,
                english_brand_name,
                customer_service_name,
                customer_service_opening,
                customer_service_closing,
                customer_service_number,
                created_at,
                updated_at,
                image_url,
                background_image_url,
                introduce,
                description,
                postal_code,
                address,
                address_detail,
                delivery_information,
                refund_information,
                is_delete
            )
            VALUES(
                %(user_info_id)s,
                %(seller_category_id)s,
                %(korean_brand_name)s,
                %(english_brand_name)s,
                %(customer_service_name)s,
                %(customer_service_opening)s,
                %(customer_service_closing)s,      
                %(customer_service_number)s,
                NOW(),
                NOW(),
                %(image_url)s,
                %(background_image_url)s,
                %(introduce)s,
                %(description)s,
                %(postal_code)s,
                %(address)s,
                %(address_detail)s,
                %(delivery_information)s,
                %(refund_information)s,
                0
            )  
            """
            cursor.execute(create_seller, seller_info)
            new_seller_log_id = cursor.lastrowid
            return new_seller_log_id

    def create_seller_log(self, seller_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            INSERT INTO seller_logs(
                seller_id,
                seller_category_id,
                korean_brand_name,
                english_brand_name,
                customer_service_name,
                customer_service_opening,
                customer_service_closing,
                customer_service_number,
                created_at,
                updated_at,
                image_url,
                background_image_url,
                introduce,
                description,
                postal_code,
                address,
                address_detail,
                delivery_information,
                refund_information,
                is_delete,
                changer_id,
                change_date
            )
            VALUES(
                %(user_info_id)s,
                %(seller_category_id)s,
                %(korean_brand_name)s,
                %(english_brand_name)s,
                %(customer_service_name)s,
                %(customer_service_opening)s,
                %(customer_service_closing)s,      
                %(customer_service_number)s,
                NOW(),
                NOW(),
                %(image_url)s,
                %(background_image_url)s,
                %(introduce)s,
                %(description)s,
                %(postal_code)s,
                %(address)s,
                %(address_detail)s,
                %(delivery_information)s,
                %(refund_information)s,
                0,
                %(user_info_id)s,
                NOW()
            )  
            """
            cursor.execute(query, seller_info)
            new_seller_log_id = cursor.lastrowid
            return new_seller_log_id

    def login_seller(self, seller_login_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT 
                    id,
                    user_type_id,
                    username, 
                    phone_number,
                    password, 
                    is_delete
                FROM 
                    user_info
                WHERE 
                    username = %(username)s 
            """
            cursor.execute(query, seller_login_info)
            seller = cursor.fetchone()
            return seller

    def create_seller_user_info(self, seller_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO user_info(
                    user_type_id,
                    username,
                    phone_number,
                    password,
                    is_delete
                )
                VALUES(
                    %(user_type_id)s,
                    %(username)s,
<<<<<<< HEAD
                    %(phone_number)s,
=======
                    %(phoneNumber)s,
>>>>>>> b17f311... [어드민] seller 상세정보 수정
                    %(password)s,
                    0
                )
            """
            cursor.execute(query, seller_info)
            new_seller_id = cursor.lastrowid
            return new_seller_id

    def create_seller_user_info_log(self, seller_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO user_info_logs(
                    user_info_id,
                    user_type_id,
                    username,
                    phone_number,
                    password,
                    changer_id,
                    change_date
                )
                VALUES(
                    %(user_info_id)s,
                    %(user_type_id)s,
                    %(username)s,
<<<<<<< HEAD
                    %(phone_number)s,
=======
                    %(phoneNumber)s,
>>>>>>> b17f311... [어드민] seller 상세정보 수정
                    %(password)s,
                    %(user_info_id)s,
                    NOW()
                )
            """
            cursor.execute(query, seller_info)
            new_seller_log_id = cursor.lastrowid
            return new_seller_log_id

<<<<<<< HEAD
#채현님 코드
    def seller_edit_get_dao(self, user_id, connection):
=======
#채현 : 정보수정페이지 내용 가져오기 (get)
    def seller_edit_get_dao(self, user, connection):
>>>>>>> b17f311... [어드민] seller 상세정보 수정
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            get_info = """
                SELECT
                    u.username,
<<<<<<< HEAD
                    s.korean_brand_name AS brandKoreand,
                    s.english_brand_name AS brandEnglish,
                    s.image_url AS profile,
=======
                    s.korean_brand_name AS brandKorean,
                    s.english_brand_name AS brandEnglish,
                    s.image_url AS profile,
                    sl.name AS sellerStatus,
                    sc.name AS sellerCategory,
>>>>>>> b17f311... [어드민] seller 상세정보 수정
                    s.background_image_url AS backgroundImage,
                    s.introduce,
                    s.description,
                    s.customer_service_name AS customerServiceName,
                    CAST(s.customer_service_opening AS CHAR) AS customerServiceOpen,
                    CAST(s.customer_service_closing AS CHAR) AS customerServiceClose,
                    s.customer_service_number AS customerServicePhone,
                    s.postal_code AS postal,
                    s.address,
                    s.address_detail AS addressDetail,
                    s.delivery_information AS deliveryInfo,
                    s.refund_information AS refundInfo
                FROM
                    sellers AS s
                INNER JOIN
                    user_info AS u
                    ON
                        s.user_info_id = u.id
<<<<<<< HEAD
                WHERE
                    s.user_info_id = %(user_id)s
            """
            cursor.execute(get_info, {"user_id": user_id})

            return cursor.fetchone()

    def get_seller_manager(self, user_id, connection):
=======
                JOIN
                    seller_level_types AS sl
                    ON
                    s.seller_level_type_id  = sl.id
                JOIN
                    seller_categories AS sc
                    ON
                    s.seller_category_id = sc.id
                WHERE
                    s.user_info_id = %(user_id)s
            """
            cursor.execute(get_info, {"user_id": user['user_id']})

            return cursor.fetchone()
# 채현 : seller의 manager 정보 가져오기
    def get_seller_manager(self, user, connection):
>>>>>>> b17f311... [어드민] seller 상세정보 수정
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            manager_info = """
                SELECT
                    m.id,
                    m.name,
                    m.email,
<<<<<<< HEAD
                    m.phone_number
=======
                    m.phone_number AS phoneNumber
>>>>>>> b17f311... [어드민] seller 상세정보 수정
                FROM
                    managers AS m
                WHERE
                    m.seller_id = %(user_id)s
<<<<<<< HEAD

            """
            cursor.execute(manager_info, {"user_id": user_id})

            return cursor.fetchall()

    # 수정화면을 처음 들어갔는지 확인하는 쿼리문(처음이라면 모든 값이 null)
    def find_seller_info(self, user_id, connection):
=======
                    AND
                    is_delete = 0

            """
            cursor.execute(manager_info, {"user_id": user['user_id']})

            return cursor.fetchall()
# 채현 : seller의 정보수정내용 중 필수입력란만 확인하기
    # 수정화면을 처음 들어갔는지 확인하는 쿼리문(처음이라면 모든 값이 null)
    def find_seller_info(self, user, connection):
>>>>>>> b17f311... [어드민] seller 상세정보 수정
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            find_info = """
                SELECT
                    s.image_url,
                    s.introduce,
                    s.customer_service_opening,
                    s.customer_service_closing,
                    s.address,
                    s.delivery_information,
                    s.refund_information
                FROM
                    sellers AS s
                LEFT JOIN
                    managers AS m
                ON
                    m.seller_id = s.user_info_id
                WHERE
                    s.user_info_id = %(user_id)s
            """
<<<<<<< HEAD
            cursor.execute(find_info, {"user_id": user_id})
            find = cursor.fetchall()

            return find

=======
            cursor.execute(find_info, {"user_id": user['user_id']})

            return cursor.fetchone()
# 채현 : 들어온 값들에 대해 update 해주기 (patch)
>>>>>>> b17f311... [어드민] seller 상세정보 수정
    def update_information(self, seller_edit_info, connection):
        """
        주석 추가 (# 필수입력 정보가 모두 작성되있던 상태에서 일부 값들을 수정할 경우(매니저 제외)) RESTFUL
        """
<<<<<<< HEAD
        print('??????????????????????????????????')
=======
>>>>>>> b17f311... [어드민] seller 상세정보 수정
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                UPDATE
                    sellers
                SET
            """
            if seller_edit_info['profile']:
                query += """
                    image_url = %(profile)s,
                """
            if seller_edit_info['introduce']:
                query += """
                    introduce = %(introduce)s,
                """
            if seller_edit_info['description']:
                query += """
                    description = %(description)s,
                """
            if seller_edit_info['postalCode']:
                query += """
                    postal_code = %(postalCode)s,
                """
            if seller_edit_info['address']:
                query += """
                    address = %(address)s,
                """
            if seller_edit_info['detailAddress']:
                query += """
                    address_detail = %(detailAddress)s,
                """
            if seller_edit_info['delivery_info']:
                query += """
                    delivery_info = %(delivery_info)s,
                """
            if seller_edit_info['refund_info']:
                query += """
                    refund_info = %(refund_info)s,
                """
            if seller_edit_info['callName']:
                query += """
                    customer_service_name = %(callName)s,
                """
            if seller_edit_info['callStart']:
                query += """
                    customer_service_opening = %(callStart)s,
                """
            if seller_edit_info['callEnd']:
                query += """
                    customer_service_closing = %(callEnd)s,
                """
<<<<<<< HEAD
=======
            if seller_edit_info['brandKorean']:
                query += """
                    korean_brand_name = %(brandKorean)s,
                """
            if seller_edit_info['brandEnglish']:
                query += """
                    english_brand_name = %(brandEnglish)s,
                """
            if seller_edit_info['service_open']:
                query += """
                    customer_service_opening = %(service_open)s,
                """
            if seller_edit_info['service_close']:
                query += """
                    customer_serivce_closing = %(service_close)s,
                """
>>>>>>> b17f311... [어드민] seller 상세정보 수정
            query += """
                    updated_at = now()
                WHERE
                    user_info_id = %(user_id)s
            """

            cursor.execute(query, seller_edit_info)

<<<<<<< HEAD
            # 새로 변경된 값이 담긴 배열 생성 (token으로 부터 받은 user_id도 포함됨)
            values = [a for a in seller_edit_info.values()]
            changed_value = []
            for row in values:
                if row is not None:
                    changed_value.append(row)

            # 실제로 새로 입력받은 seller의 정보갯수 반환
            return len(changed_value) - 1

    # 수정되는 유저에 배당된 is_delete=0 인 매니저의 수 파악
    def check_seller_manager(self, user_id, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            check_manager_query = """
=======
            # # 새로 변경된 값이 담긴 배열 생성 (token으로 부터 받은 user_id도 포함됨)
            # values = [a for a in seller_edit_info.values()]
            # changed_value = []
            # for row in values:
            #     if row is not None:
            #         changed_value.append(row)

            # # 실제로 새로 입력받은 seller의 정보갯수 반환
            # return len(changed_value) - 1
            return cursor.lastrowid

    # 수정되는 유저에 배당된 is_delete=0 인 매니저의 수 파악
    def check_seller_manager_number(self, user, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            check_manager_number = """
>>>>>>> b17f311... [어드민] seller 상세정보 수정
                SELECT
                    COUNT(*)
                FROM
                    managers AS m
                WHERE
<<<<<<< HEAD
                    m.user_info_id = %(user_id)s
                    AND
                    m.is_delete=0
            """
            cursor.execute(check_manager_query, {"user_id": user_id})
=======
                    m.seller_id = %(user_id)s
                    AND
                    m.is_delete=0
            """
            cursor.execute(check_manager_number, {"user_id": user['user_id']})
>>>>>>> b17f311... [어드민] seller 상세정보 수정

            return cursor.fetchone()

    # 들어온 값 중이 이미 존재하는 값이 있을 경우 에러 반환
    def check_seller_manager(self, seller_edit_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            manager_query = """
                    SELECT
                        m.id,
                        m.name,
                        m.email,
                        m.phone_number
                    FROM
                        managers AS m
                    WHERE
                        m.seller_id = %(user_id)s
                        AND
                        is_delete = 0
                """
            cursor.execute(manager_query, {"user_id": seller_edit_info['user_id']})
            return cursor.fetchall()

    # 이미 작성된 manager의 정보 수정
    def update_manager(self, one, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            edit_manager = """
                UPDATE
                    managers
                SET
<<<<<<< HEAD
            """
            if one['name']:
                edit_manager += """
                    name = %(name)s,
                """
            if one['email']:
                edit_manager += """
                    email = %(email)s,
                """
            if one['phone']:
                edit_manager += """
                    phone_number = %(phone)s,
                """
            edit_manager += """
                updated_at = now()
            """

            cursor.execute(edit_manager, one)
            return cursor.fetchone()
=======
                    name = %(name)s,
                    email = %(email)s,
                    phone_number = %(phoneNumber)s,
                    updated_at = now()
                WHERE
                    id = %(id)s
            """
            cursor.execute(edit_manager, one)
            return True
>>>>>>> b17f311... [어드민] seller 상세정보 수정

    # 들어온 값에 대한 manager 신규 생성
    def insert_information_manager(self, one, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
<<<<<<< HEAD
            print('dao에서 받는 one=====', one)
=======
>>>>>>> b17f311... [어드민] seller 상세정보 수정
            manager_query = """
                    INSERT INTO
                        managers
                        (
                            seller_id,
                            name,
                            email,
                            phone_number
                        )
                        VALUES
                        (
                            %(user_id)s,
                            %(name)s,
                            %(email)s,
<<<<<<< HEAD
                            %(phone)s
=======
                            %(phoneNumber)s
>>>>>>> b17f311... [어드민] seller 상세정보 수정
                        )
            """
            cursor.execute(manager_query, one)
            return cursor.lastrowid

<<<<<<< HEAD
    def create__manager_logs(self, one, connection):
=======
    def delete_manager_dao(self, man_id, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            delete_query = """
                UPDATE
                    managers
                SET
                    is_delete = 1
                WHERE
                    id IN %(man_id)s
            """
            cursor.execute(delete_query, {"man_id" : man_id})
            return True

    def create_manager_log(self, extra, connection):
>>>>>>> b17f311... [어드민] seller 상세정보 수정
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            log_query = """
                INSERT INTO
                    manager_logs(
<<<<<<< HEAD
                        name,
                        email,
                        phone_number,
                        seller_id
                    )
                SELECT
                    m.name,
                    m.email,
                    m.phone_number,
                    %(user_id)s
                FROM
                    managers AS m
                )

            """

    # seller_logs 생성
    def create_seller_update_log(self, user_id, connection):
=======
                        manager_id,
                        name,
                        email,
                        phone_number,
                        created_at,
                        updated_at,
                        seller_id,
                        changer_id,
                        change_date
                    )
                SELECT
                    m.id,
                    m.name,
                    m.email,
                    m.phone_number,
                    m.created_at,
                    m.updated_at,
                    m.seller_id,
                    %(user_id)s,
                    now()
                FROM
                    managers AS m
                WHERE
                    m.id = %(changeId)s
            """
            cursor.execute(log_query, {"changeId" :extra['changeId'], "user_id" : extra['user_id']})
            return "ok"

    # seller_logs 생성
    def create_seller_update_log(self, user, connection):
>>>>>>> b17f311... [어드민] seller 상세정보 수정
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            log_query = """
                INSERT INTO
                    seller_logs(
                        seller_id,
                        seller_tier_type_id,
                        seller_category_id,
                        seller_level_type_id,
                        korean_brand_name,
                        english_brand_name,
                        customer_service_name,
<<<<<<< HEAD
                        customer_serice_opening,
=======
                        customer_service_opening,
>>>>>>> b17f311... [어드민] seller 상세정보 수정
                        customer_service_closing,
                        customer_service_number,
                        created_at,
                        updated_at,
                        image_url,
                        background_image_url,
                        introduce,
                        description,
                        postal_code,
                        address,
                        address_detail,
                        is_weekend,
                        delivery_information,
                        refund_information,
                        is_delete,
                        changer_id,
                        change_date
                    )
                    SELECT
                        s.user_info_id,
                        s.seller_tier_type_id,
                        s.seller_category_id,
                        s.seller_level_type_id,
                        s.korean_brand_name,
                        s.english_brand_name,
                        s.customer_service_name,
                        s.customer_service_opening,
                        s.customer_service_closing,
                        s.customer_service_number,
                        s.created_at,
                        s.updated_at,
                        s.image_url,
                        s.background_image_url,
                        s.introduce,
                        s.description,
                        s.postal_code,
                        s.address,
                        s.address_detail,
                        s.is_weekend,
                        s.delivery_information,
                        s.refund_information,
                        s.is_delete,
<<<<<<< HEAD
                        %(user_id)s,
=======
                        %(changer_id)s,
>>>>>>> b17f311... [어드민] seller 상세정보 수정
                        now()
                    FROM
                        sellers AS s
                    WHERE
                        s.user_info_id = %(user_id)s
                """
<<<<<<< HEAD
            cursor.execute(log_query, {"user_id": user_id})

            return cursor.fetchone()

=======
            cursor.execute(log_query, {"user_id" : user['user_id'], "changer_id": user['changer_id']})

            return True
>>>>>>> b17f311... [어드민] seller 상세정보 수정
from typing import List


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    cursor = con.cursor()
    cursor.execute(
        '''INSERT INTO Customers
           (CustomerName, ContactName, Address, City, PostalCode, Country)
           VALUES (%s, %s, %s, %s, %s, %s)''',
        ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore')
    )
    con.commit()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute("SELECT * FROM Customers")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("SELECT * FROM Customers WHERE Country = %s", ('Germany',))
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        con: psycopg connection

    Returns: 91 records with updated customer

    """
    cur = con.cursor()
    cur.execute(
        '''UPDATE Customers SET CustomerName = %s 
           WHERE CustomerId = (SELECT CustomerId FROM Customers LIMIT %s)''',
        ('Johnny Depp', 1)
    )
    con.commit()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    cur = con.cursor()
    cur.execute(
        '''DELETE FROM Customers 
           WHERE CustomerId = (SELECT CustomerId FROM Customers ORDER BY CustomerId DESC LIMIT %s)''',
        (1,)
    )
    con.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute('SELECT Country FROM Suppliers')
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute('SELECT Country FROM Suppliers ORDER BY Country DESC')
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    cur.execute("SELECT COUNT(CustomerId), City FROM Customers GROUP BY City")
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("SELECT COUNT(CustomerId), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerId) > %s", (10,))
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute("SELECT * FROM Customers LIMIT %s", (10,))
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("SELECT * FROM Customers OFFSET %s", (11,))
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    cur.execute(
        '''SELECT SupplierId, SupplierName, ContactName, City, Country FROM Suppliers 
           WHERE Country in (%s, %s, %s)''',
        ('USA', 'UK', 'Japan')
    )
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute(
        '''SELECT p.ProductName FROM Products p 
           JOIN Suppliers s ON p.SupplierID = s.SupplierID 
           WHERE s.Country = %s''',
        ('Sweden',)
    )
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute(
        '''SELECT p.ProductId, p.ProductName, p.Unit, p.Price, s.Country, s.City, s.SupplierName 
           FROM Products p 
           JOIN Suppliers s ON p.SupplierID = s.SupplierID'''
    )
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute(
        '''SELECT c.CustomerName, c.ContactName, c.Country, o.OrderId FROM Orders o 
           JOIN Customers c ON c.CustomerID = o.CustomerID'''
    )
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    cur.execute(
        '''SELECT c.CustomerName, c.Address, c.Country as customerCountry, s.Country as supplierCountry, s.SupplierName as supplierName 
           FROM Customers c FULL OUTER JOIN Suppliers s ON s.Country = c.Country ORDER BY customerCountry, supplierCountry'''
    )
    return cur.fetchall()

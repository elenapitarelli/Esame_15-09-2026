from database.DB_connect import DBConnect
from model.airport import Airport
from model.connessione import Connessione

class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_all_airports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_nodes(n_voli):
        cnx = DBConnect.get_connection()

        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = """ select distinct a.state
                    from airports a , flights f
                    where a.id = f.id 
                    group by a.state
                    having count(f.id) >= 1"""
        try:
            cursor.execute(query, (n_voli,))
            for row in cursor:
                airport = Airport(**row)
                result.append(airport)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_connessioni(n_voli):
        cnx = DBConnect.get_connection()

        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = """ select distinct a1.STATE as state1, a2.STATE as state2, count(distinct f1.id) as peso
                    from airports a1, airports a2, flights f1, flights f2, airlines ai1, airlines ai2
                    where a1.ID != a2.ID and a1.ID = f1.ORIGIN_AIRPORT_ID and a2.id = f2.DESTINATION_AIRPORT_ID and ai1.ID =ai2.ID and a1.STATE != a2.STATE
                    group by state1, state2 """
        try:
            cursor.execute(query, (n_voli,))
            for row in cursor:
                connessione = Connessione(**row)
                result.append(connessione)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
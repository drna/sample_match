import psycopg2
import pandas as pds
from sqlalchemy import create_engine
from sqlalchemy.engine import interfaces


class PostgreInterface():

    def __init__(self) -> None:
        self.alchemy_engine = create_engine(
            'postgresql+psycopg2://postgres:admin@localhost/postgres', pool_recycle=3600)

        self.dbConnection = self.alchemy_engine.connect()
        return

    def read_dataFrame(self) -> pds.DataFrame:
        dataFrame = pds.read_sql(
            "select * from \"newTable2\"", self.dbConnection)
        pds.set_option('display.expand_frame_repr', False)

        # Print the dataFrame for debugging
        print(dataFrame)
        return dataFrame

    def store_dataFrame(self, dataFrame: pds.DataFrame, db_table_name: str) -> bool:
        try:
            frame = dataFrame.to_sql(
                db_table_name, self.dbConnection, if_exists='fail')
        except ValueError as vx:
            print(vx)
            return False
        except Exception as ex:
            print(ex)
            return False
        else:
            print("PostgreSQL Table %s has been created successfully." %
                  dbTableName)
        finally:
            return True


interface = PostgreInterface()

# Data - Marks scored

test = [(1, 2, 2, 2, 2),
        (2, 1, 0, 1, 3),
        (3, 0, 2, 1, 1)
        ]

# Create a DataFrame
dataFrame = pds.DataFrame(test,
                          index=("212090T1A_337-CHPv6_week24run3-21",
                                 "212090T1A_337-CHPv6_week24run3-21", "212090T1A_337-CHPv6_week24run3-21"),
                          columns=("test1", "test2", "test3", "test4", "test5")
                          )

interface.store_dataFrame(dataFrame, "newTable2")
interface.read_dataFrame()

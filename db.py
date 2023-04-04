from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# engine permite a SQLAlchemy comunicarse con la base de datos


engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread':False})
# Advertencia, crear el engine noconecta inmediatamente a la base de datos, eso lo hacemos después

# sesión la creamos para permitirnos  realizar transacciones (operaciones) dentro de nuestra BD
Session = sessionmaker(bind=engine)
session = Session()

# vinculación
Base = declarative_base()
# Ahora vamos al fichero modelos.py y en los modelos (clases) donde queremos que se transformen en tablas, le añadiremos esta
#variable, y esto se encargará de mapear y vincular la clase a la tabla
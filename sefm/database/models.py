from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func
from sqlalchemy import Column, Date, Integer, String, REAL, DateTime, ForeignKey
import os

from config import Config

Base = declarative_base()


class region(Base):
    __tablename__ = 'region'
    __table_args__ = {'extend_existing': True}
    id_region = Column('id_region', Integer, primary_key=True)
    nom_region = Column('nom_region', String)
    value = Column('value', REAL)

    def __repr__(self):
        return '<date {}>'.format(self.value)


class station(Base):
    __tablename__ = 'station'
    __table_args__ = {'extend_existing': True}
    id_station = Column('id_station', Integer, primary_key=True)
    numero_station = Column('numero_station', String)
    province = Column('province', String)
    latitude = Column('latitude', REAL)
    longitude = Column('longitude', REAL)

    def __repr__(self):
        return '<amenagement {}>'.format(self.nom_amenagement)


# class concatenations(Base):
#     __tablename__ = 'concatenations'
#     __table_args__ = {'extend_existing': True}
#     bassin_concatene = Column('bassin_concatene', UUID(as_uuid=True), primary_key=True)
#     bassin_inclus = Column('bassin_inclus', UUID(as_uuid=True), primary_key=True)
#
#     def __repr__(self):
#         return '<concat {}>'.format(self.bassin_concatene)
#
#
# class bassin(Base):
#     __tablename__ = 'bassin'
#     __table_args__ = {'extend_existing': True}
#     # id_bassin = Column('id_bassin', Integer, primary_key=True, unique=True)
#     uid = Column('uid', UUID(as_uuid=True), primary_key=True,
#                     default=sqlalchemy.text("uuid_generate_v4()"))
#     numero_station = Column('numero_station', String, unique=True)
#     nom_station = Column('nom_station', String)
#     nom_equiv = Column('nom_equivalent', String)
#     province = Column('province', String)
#     regime = Column('regularisation', String)
#     superficie = Column('superficie', Integer)
#     latitude = Column('latitude', REAL)
#     longitude = Column('longitude', REAL)
#     geometry = Column('geometry', Geometry(geometry_type='POLYGON', srid=4326))
#     point = Column('latlon', Geometry(geometry_type='POINT', srid=4326))
#
#     def __repr__(self):
#         return '<basins {}>'.format(self.uid)
#
#
# class meta_series(Base):
#     __tablename__ = 'meta_series'
#     __table_args__ = {'extend_existing': True}
#     id = Column('id', Integer, primary_key=True, unique=True)
#     uid = Column('uid', UUID(as_uuid=True))
#     type_serie = Column('type_serie', String)
#     pas_de_temps = Column('pas_de_temps', String)
#     aggregation = Column('aggregation', String)
#     unites = Column('unites', String)
#     date_debut = Column('date_debut', DateTime(timezone=True))
#     date_fin = Column('date_fin', DateTime(timezone=True))
#     source = Column('source', String)
#
#     def __repr__(self):
#         return '<meta_ts {}>'.format(self.id)
#
#
# class don_series(Base):
#     __tablename__ = 'don_series'
#     __table_args__ = {'extend_existing': True}
#     id = Column('id', Integer, ForeignKey(meta_series.id), primary_key=True)
#     date = Column('date', DateTime(timezone=True), primary_key=True)
#     value = Column('value', REAL)
#
#     def __repr__(self):
#         return '<date {}>'.format(self.value)

def create_db():
    if not os.path.isfile(Config.DATABASE_FILE):
        print('test')
        engine = create_engine(Config.DATABASE_URI, echo=True)
        Base.metadata.create_all(engine)

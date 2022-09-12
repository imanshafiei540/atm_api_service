"""empty message

Revision ID: cbf894bf3ce5
Revises: 
Create Date: 2022-09-12 12:22:03.305440

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision = 'cbf894bf3ce5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base_geometries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('coordinates', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('geometry_coordinates', Geometry(srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('atm_devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=450), nullable=True),
    sa.Column('provider', sa.String(length=50), nullable=True),
    sa.Column('geometry_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['geometry_id'], ['base_geometries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_table('atm_devices')
    op.drop_table('base_geometries')
    # ### end Alembic commands ###

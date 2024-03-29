"""empty message

Revision ID: 084718529b4a
Revises: 
Create Date: 2024-02-20 17:21:48.816641

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '084718529b4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=True),
    sa.Column('apellidos', sa.String(length=120), nullable=True),
    sa.Column('tipo_identificacion', sa.String(length=4), nullable=True),
    sa.Column('numero_identificacion', sa.Integer(), nullable=True),
    sa.Column('registro_medico', sa.Integer(), nullable=True),
    sa.Column('especialidad', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('medicos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medicos',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('medico')
    # ### end Alembic commands ###

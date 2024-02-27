"""empty message

Revision ID: 783b47cd7049
Revises: 
Create Date: 2024-02-27 14:45:45.996485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '783b47cd7049'
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
    op.create_table('paciente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=True),
    sa.Column('apellidos', sa.String(length=120), nullable=True),
    sa.Column('tipo_identificacion', sa.String(length=4), nullable=True),
    sa.Column('numero_identificacion', sa.Integer(), nullable=True),
    sa.Column('altura', sa.Integer(), nullable=True),
    sa.Column('tipo_sangre', sa.String(length=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('paciente')
    op.drop_table('medico')
    # ### end Alembic commands ###

"""TabelaTarefas

Revision ID: c035ef95c9a7
Revises: 
Create Date: 2025-01-08 12:26:25.454086

"""
from alembic import op
import sqlalchemy as sa

revision: str = 'c035ef95c9a7'
down_revision= None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Criação da tabela tarefas
    op.create_table(
        'tarefas',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('titulo', sa.String(length=50), nullable=False),
        sa.Column('descricao', sa.String(length=50), nullable=True),
        sa.Column('estado', sa.String(length=20), nullable=False),
        sa.Column('data_criacao', sa.DateTime(), nullable=False),
        sa.Column('data_atualizacao', sa.DateTime(), nullable=False)
    )

def downgrade() -> None:
    # Exclusão da tabela tarefas
    op.drop_table('tarefas')

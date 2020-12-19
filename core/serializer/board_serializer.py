import uuid

from rest_framework import serializers
from core.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['owner', 'board_id', 'board_name', 'board_class', 'public']
        read_only_fields = ['owner', 'board_id']
        depth = 0

    def create(self, validated_data):
        profile = self.context.get('student_profile')
        board = Board.objects.create(
            board_id=str(uuid.uuid4()),
            board_name=validated_data['board_name'],
            board_class=validated_data['board_class'],
            public=validated_data['public'],
            owner=profile,
        )

        board.save()

        return board

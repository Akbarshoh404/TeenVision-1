from rest_framework import serializers
from core.models import Program, Major


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

    def validate(self, data):
        if data.get('type') == 'tutorial':
            for field in ['type', 'title', 'photo', 'link']:
                if not data.get(field):
                    raise serializers.ValidationError({field: "Bu maydonni to'ldirish majburiy"})
        return data


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'

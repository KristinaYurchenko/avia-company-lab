from plane_app.models import Airplane


class AirplaneDAO:
    @staticmethod
    def get_all():
        return Airplane.objects.all()

    @staticmethod
    def get_by_id(airplane_id):
        return Airplane.objects.get(id=airplane_id)

    @staticmethod
    def create(**kwargs):
        return Airplane.objects.create(**kwargs)

    @staticmethod
    def update(airplane, **kwargs):
        for key, value in kwargs.items():
            setattr(airplane, key, value)
        airplane.save()
        return airplane

    @staticmethod
    def delete(airplane):
        airplane.delete()

from plane_app.dao.airplane import AirplaneDAO


class AirplaneService:

    def get_all_airplanes(self):
        return AirplaneDAO.get_all()

    def get_airplane(self, airplane_id):
        return AirplaneDAO.get_by_id(airplane_id)

    def create_airplane(self, data):
        return AirplaneDAO.create(**data)

    def update_airplane(self, airplane_id, data):
        airplane = AirplaneDAO.get_by_id(airplane_id)
        if airplane:
            return AirplaneDAO.update(airplane, **data)
        return None

    def delete_airplane(self, airplane_id):
        airplane = AirplaneDAO.get_by_id(airplane_id)
        if airplane:
            AirplaneDAO.delete(airplane)
            return True
        return False

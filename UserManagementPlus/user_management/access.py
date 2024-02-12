# определить класс AccessControl с методами grant_access() и revoke_access()
# (Можно также расширить системы управления правами доступа: для этого нужно
# расширить методы класса AccessControl для поддержки новых ролей и функциональности)

# access.py
class AccessControl:
    @staticmethod
    def grant_access(user, role):
        # Реализуйте предоставление доступа в зависимости от роли пользователя
        pass

    @staticmethod
    def revoke_access(user, role):
        # Реализуйте отзыв доступа в зависимости от роли пользователя
        pass

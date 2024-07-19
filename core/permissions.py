from rest_framework import permissions

class GlobalDefaultPermission(permissions.BasePermission):
    """
    Permissões globais para modelos
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário tem permissão para a ação solicitada.
        """
        # Permite acesso aos métodos GET, HEAD e OPTIONS para qualquer usuário autenticado
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # Obtém o codinome da permissão com base no método HTTP e na view
        model_permission_codename = self.__get_model_permission_codename(request.method, view)

        # Se não for possível determinar o codinome da permissão, nega o acesso
        if not model_permission_codename:
            return False

        # Verifica se o usuário tem a permissão necessária
        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        """
        Obtém o codinome da permissão para um método HTTP e uma view específicos.
        """
        try:
            # Obtém o nome do modelo e o rótulo do aplicativo a partir do queryset da view
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label

            # Determina a ação (view, add, change, delete) com base no método HTTP
            action = self.__get_action_suffix(method)

            # Retorna o codinome da permissão no formato 'app_label.action_model_name'
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            # Retorna None se ocorrer um AttributeError, indicando que não foi possível determinar o modelo ou o app_label
            return None

    def __get_action_suffix(self, method):
        """
        Mapeia métodos HTTP para sufixos de ação de permissão.
        """
        # Dicionário que mapeia métodos HTTP para sufixos de ação
        method_actions = {
            'GET': 'view',       # Método GET mapeado para 'view'
            'POST': 'add',       # Método POST mapeado para 'add'
            'PUT': 'change',     # Método PUT mapeado para 'change'
            'PATCH': 'change',   # Método PATCH mapeado para 'change'
            'DELETE': 'delete',  # Método DELETE mapeado para 'delete'
            'OPTIONS': 'view',   # Método OPTIONS mapeado para 'view'
            'HEAD': 'view',      # Método HEAD mapeado para 'view'
        }

        # Retorna o sufixo de ação correspondente ao método HTTP, ou uma string vazia se o método não estiver no dicionário
        return method_actions.get(method, '')

from .Scene import Scene
from ..cache import Cache
from .Views.ViewRouter import ViewRouter


class RadioChannelsScene(Scene):
    def __init__(self, scene_router):
        super(RadioChannelsScene, self).__init__(scene_router, "radiochannels", "Radio Channels Scene")

        self.cache = Cache("RadioChannelsScene")

        view_router = ViewRouter(self)
        view = view_router.route(self.scene_router.get_path(self))
        view_router.root.set_lazy_radios(lambda: self.cache.get('radios', default_producer=self.scene_router.api.get_radios))
        self.set_view(view)

        self.cache.save()

from ...domain.models.operations import OperationalContext, WeatherState, Stadium
from ...domain.enums.operations import WeatherCondition

class ContextService:
    async def get_current_context(self) -> OperationalContext:
        # In a real app, this fetches from the DB/live telemetry
        return OperationalContext(
            stadium=Stadium(name="Main Stadium", capacity=50000, current_occupancy=42000),
            weather=WeatherState(condition=WeatherCondition.RAIN, temperature_celsius=18.0, wind_speed_kmh=15),
            gates=[],
            facilities=[],
            medical_units=[],
            active_incidents=[]
        )

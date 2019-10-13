from flask import g

from src.db_models.activity import Activity


class ActivityRepository:

    def add(
            self,
            athlete_id,
            type,
            date,
            distance,
            duration,
            ):
        activity = Activity(
            athlete_id=athlete_id,
            type=type,
            date=date,
            distance=distance,
            duration=duration
        )
        g.db.session.add(activity)
        g.db.session.commit()

    def fetch_all_activities_by_athlete_id(self, athlete_id):
        return g.db.session.query(Activity).filter_by(athlete_id=athlete_id).all()

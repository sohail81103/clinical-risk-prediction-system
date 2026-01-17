from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from utils.database import Base

class PatientPrediction(Base):
    __tablename__ = "patient_predictions"

    id = Column(Integer, primary_key=True, index=True)

    radius_mean = Column(Float)
    texture_mean = Column(Float)
    perimeter_mean = Column(Float)
    area_mean = Column(Float)
    smoothness_mean = Column(Float)
    compactness_mean = Column(Float)
    concavity_mean = Column(Float)
    concave_points_mean = Column(Float)
    symmetry_mean = Column(Float)
    fractal_dimension_mean = Column(Float)

    radius_se = Column(Float)
    texture_se = Column(Float)
    perimeter_se = Column(Float)
    area_se = Column(Float)
    smoothness_se = Column(Float)
    compactness_se = Column(Float)
    concavity_se = Column(Float)
    concave_points_se = Column(Float)
    symmetry_se = Column(Float)

    diagnosis = Column(String)
    confidence = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

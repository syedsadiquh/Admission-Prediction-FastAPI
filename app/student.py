from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str
    gre: float = Field(gt=0, alias="GRE Score")
    toefl: float = Field(gt=0, alias="TOEFL Score")
    university_rating: float = Field(gt=0, lt=6, alias="University Rating")
    sop: float = Field(gt=0, lt=6, alias="SOP Strength (1-5)")
    lor: float = Field(gt=0, lt=6, alias="LOR Strength (1-5)")
    cgpa: float = Field(gt=0, lt=10.1,alias="CGPA")
    research: bool = Field(alias="Research Done")
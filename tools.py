## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from pypdf import PdfReader

from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class BloodTestReportInput(BaseModel):
    """Input schema for Blood Test Report Tool."""
    path: str = Field(default='data/sample.pdf', description="Path to the PDF file containing the blood test report")


class BloodTestReportTool(BaseTool):
    name: str = "Blood Test Report Tool"
    description: str = "Reads and extracts blood test report data from PDF files. Cleans and formats the content for analysis."
    args_schema: Type[BaseModel] = BloodTestReportInput
    
    def _run(self, path: str = 'data/sample.pdf') -> str:
        """Tool to read data from a pdf file from a path
        
        Args:
            path (str): Path of the pdf file. Defaults to 'data/sample.pdf'.
            
        Returns:
            str: Full Blood Test report content
        """
        try:
            full_report = ""
            
            with open(path, 'rb') as file:
                pdf_reader = PdfReader(file)
                
                # Extract text content from all pages
                for page_num, page in enumerate(pdf_reader.pages):
                    content = page.extract_text()
                    
                    # Clean and format the report data
                    # Remove extra whitespaces and format properly
                    while "\n\n" in content:
                        content = content.replace("\n\n", "\n")
                    
                    full_report += content + "\n"
                    print(full_report)
            
            return full_report.strip()
            
        except Exception as e:
            return f"Error reading blood test report: {str(e)}"
## Creating Nutrition Analysis Tool
class NutritionAnalysisInput(BaseModel):
    """Input schema for Nutrition Analysis Tool."""
    blood_report_data: str = Field(description="Blood test report data to analyze for nutrition recommendations")


class NutritionTool(BaseTool):
    name: str = "Nutrition Analysis Tool"
    description: str = "Analyzes blood test report data and provides personalized nutrition recommendations based on the results."
    args_schema: Type[BaseModel] = NutritionAnalysisInput
    
    def _run(self, blood_report_data: str) -> str:
        """Tool to analyze blood report data and provide nutrition recommendations
        
        Args:
            blood_report_data (str): Blood test report data to analyze
            
        Returns:
            str: Nutrition analysis and recommendations
        """
        try:
            # Process and analyze the blood report data
            processed_data = blood_report_data
            
            # Clean up the data format
            i = 0
            while i < len(processed_data):
                if processed_data[i:i+2] == "  ":  # Remove double spaces
                    processed_data = processed_data[:i] + processed_data[i+1:]
                else:
                    i += 1
                    
            # TODO: Implement nutrition analysis logic here
            return "Nutrition analysis functionality to be implemented"
            
        except Exception as e:
            return f"Error analyzing nutrition data: {str(e)}"


## Creating Exercise Planning Tool
class ExercisePlanInput(BaseModel):
    """Input schema for Exercise Planning Tool."""
    blood_report_data: str = Field(description="Blood test report data to use for creating personalized exercise plan")


class ExerciseTool(BaseTool):
    name: str = "Exercise Planning Tool"
    description: str = "Creates personalized exercise plans based on blood test report data and health indicators."
    args_schema: Type[BaseModel] = ExercisePlanInput
    
    def _run(self, blood_report_data: str) -> str:
        """Tool to create personalized exercise plan based on blood report data
        
        Args:
            blood_report_data (str): Blood test report data to analyze
            
        Returns:
            str: Personalized exercise plan and recommendations
        """
        try:
            # TODO: Implement exercise planning logic here
            return "Exercise planning functionality to be implemented"
            
        except Exception as e:
            return f"Error creating exercise plan: {str(e)}"
"""
Course Page Object for D2L
Handles course-related functionality
"""

from playwright.sync_api import Page
from .base_page import BasePage

class CoursePage(BasePage):
    """Page Object for D2L course pages"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Course page selectors
        self.course_title = ".d2l-page-title"
        self.course_navbar = ".d2l-navbar"
        self.content_area = ".d2l-content-area" 
        self.modules_link = "a:has-text('Content')"
        self.assignments_link = "a:has-text('Assignments')"
        self.discussions_link = "a:has-text('Discussions')"
        self.gradebook_link = "a:has-text('Grades')"
        self.course_tools = ".d2l-course-tools"
        
    def get_course_title(self) -> str:
        """Get the current course title"""
        return self.get_element_text(self.course_title)
        
    def navigate_to_content(self):
        """Navigate to course content/modules"""
        self.click_element(self.modules_link)
        
    def navigate_to_assignments(self):
        """Navigate to course assignments"""
        self.click_element(self.assignments_link)
        
    def navigate_to_discussions(self):
        """Navigate to course discussions"""
        self.click_element(self.discussions_link)
        
    def navigate_to_gradebook(self):
        """Navigate to course gradebook"""
        self.click_element(self.gradebook_link)
        
    def is_in_course(self) -> bool:
        """Check if currently viewing a course"""
        return ("/d2l/le/content/" in self.get_current_url() or 
                "/d2l/home/" in self.get_current_url())
        
    def verify_course_elements(self):
        """Verify expected course elements are present"""
        assert self.is_element_visible(self.course_title), "Course title not visible"
        assert self.is_element_visible(self.course_navbar), "Course navbar not visible"
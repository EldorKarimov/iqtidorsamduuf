from modeltranslation.translator import TranslationOptions, translator
from main.models import Carousel, StartUpProjects, TalentedStudents, Documents, Competition
from courses.models import Author, Course
from news.models import NewsCategory, Tag, News

# main app translators 
class CarouselTranslationOptions(TranslationOptions):
    fields = ('content', 'content2')

class StartUpProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class TalentedStudentsTranslationOptions(TranslationOptions):
    fields = ('description', )

class DocumentsTranslationOptions(TranslationOptions):
    fields = ('file_name', )

class CompetitionTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )

translator.register(Carousel, CarouselTranslationOptions)
translator.register(StartUpProjects, StartUpProjectsTranslationOptions)
translator.register(TalentedStudents, TalentedStudentsTranslationOptions)
translator.register(Documents, DocumentsTranslationOptions)
translator.register(Competition, CompetitionTranslationOptions)


# courses app translators
class AuthorTranslationOptions(TranslationOptions):
    fields = ('bio', )

class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )

translator.register(Author, AuthorTranslationOptions)
translator.register(Course, CourseTranslationOptions)


# news app translator
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

class TagTranslationOptions(TranslationOptions):
    fields = ('name', )

class YangilikTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )

translator.register(NewsCategory, NewsCategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(News, YangilikTranslationOptions)
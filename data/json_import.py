cmd = """
import json
from Manga.models.manga import Manga
from Manga.models.chapter import Chapter
from Manga.models.category import Category
from Manga.models.content import Content

json_path = r"E:\\Tai Lieu Hoc Phan\\Nam3_KH2\\LT Python\\Project Cuoi Ky\\OkManga\\data\\manga_data.json"
with open(json_path, encoding='utf-8') as f:
    data = json.load(f)
for i,manga in enumerate(data):
    try:
        print(f"Saving manga {i+1}/{len(data)} {manga['name']}...")
        # Manga detail
        new_manga = Manga(id=manga["id"], 
                        name=manga["name"], 
                        thumbnail=manga["thumbnail"], 
                        status=manga["status"],
                        views=manga["views"],
                        chapters_number=manga["chapters_number"],
                        summary=manga["summary"])
        new_manga.save()
        # Adding categories
        for cate in manga["genres"]:
            find_genre = Category.objects.filter(category=cate.strip())
            if find_genre.count() == 0:
                new_genre = Category(category=cate.strip())
                new_genre.save()
                new_manga.category.add(new_genre)
            else:
                new_manga.category.add(find_genre[0])
        new_chapters = []
        new_contents = []
        # Adding chapters
        for ii,chapter in enumerate(manga["chapters"]):
            print(f"Chapter {ii+1}/{len(manga['chapters'])}...")
            new_chapter = Chapter(id=chapter["id"],
                                name=chapter["name"],
                                index=ii+1,
                                modified_date=chapter["modified_date"].replace("\\n","").strip(),
                                views=chapter["views"],
                                manga=new_manga)
            new_chapters.append(new_chapter)
            # Adding contents
            for content in chapter["contents"]:
                new_content = Content(chapter=new_chapter,
                                    index=content["index"],
                                    link=content["link"])
                new_contents.append(new_content)
        Chapter.objects.bulk_create(new_chapters)
        Content.objects.bulk_create(new_contents)

        # Update mode
        # Chapter.objects.bulk_update(new_chapters)
        # Content.objects.bulk_update(new_contents)
    except Exception as e:
        print(e)
        continue
print("Done!")
"""
exec(cmd)
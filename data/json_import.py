import json
from Manga.models.manga import Manga
from Manga.models.chapter import Chapter
from Manga.models.category import Category
from Manga.models.content import Content

json_path = "E:\\School\\Python\\MyManga\\mymanga\\scripts\\manga_data.json"
with open(json_path, encoding='utf-8') as f:
    data = json.load(f)
for i,manga in enumerate(data):
    print(f"Saving manga {i+1}/{len(data)} {manga['name']}...")
    # Manga detail
    new_manga = Manga(id=manga["id"], 
                    name=manga["name"], 
                    thumbnail=manga["thumbnail"], 
                    status=manga["status"],
                    views=manga["views"],
                    chapters_number=manga["chapters_number"])
    new_manga.save()
    # Adding categories
    for category in manga["genres"]:
        find_genre = Category.objects.filter(name=category.strip())
        if find_genre.count() == 0:
            new_genre = Category(name=category.strip())
            new_genre.save()
            new_manga.categories.add(new_genre)
        else:
            new_manga.categories.add(find_genre[0])
    new_chapters = []
    # Adding chapters
    for ii,chapter in enumerate(manga["chapters"]):
        print(f"Chapter {ii+1}/{len(manga['chapters'])}...")
        new_chapter = Chapter(id=chapter["id"],
                            name=chapter["name"],
                            modified_date=chapter["modified_date"].replace("\\n","").strip(),
                            views=chapter["views"],
                            manga=new_manga)
        new_chapters.append(new_chapter)
        new_contents = []
        # Adding contents
        for content in chapter["contents"]:
            new_content = Content(chapter=new_chapter,
                                index=content["index"],
                                link=content["link"])
            new_contents.append(new_content)
    Chapter.objects.bulk_create(new_chapters)
    Content.objects.bulk_create(new_contents)
print("Done!")
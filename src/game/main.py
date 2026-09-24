from src.database.queries import *

def main():
    media = get_random_media()
    media_title, media_release, media_type = media[1], media[2], media[3]
    
    actors = get_media_actors(media_title)
    directors = get_media_director(media_title)

    # Printing Type and Release
    print(f"The {media_type} was released in {media_release}")    

    # Printing the Cast
    print(f"\nThe following persons are in the cast: ")
    for actor in actors:
        print(actor)

    # Printing director(s)
    print("\nDirected by:")
    for director in directors:
        print(director)

if __name__ == "__main__":
    main()

import os
import shutil

DEST = "../source/api"

METHODS_TEMPLATE = open("template/methods.rst", encoding="UTF-8").read()
TYPES_TEMPLATE = open("template/types.rst", encoding="UTF-8").read()

def generate_documentation(
    directory: str,
    keys: list[str],
    base_class: str,
    template: str,
    auto_type: str,
):
    root = DEST + directory
    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    for key in keys:
        with open(root + f"/{key}.rst", "w") as f:
            f.write(key + "\n" + "=" * len(key) + "\n\n")
            f.write(f".. auto{auto_type}:: {base_class}.{key}()")
        template += "\n\n"
        template += ".. toctree::\n"
        template += "   :hidden:\n\n"
        template += f"   {key}"
        
    with open(root + "/index.rst", "w") as index:
        index.write(template)
        
if "__main__" == __name__:
    generate_documentation(
        directory="/methods",
        base_class="crunpyroll.Client",
        auto_type="method",
        template=METHODS_TEMPLATE,
        keys=[
            "search",
            "get_series",
            "get_seasons",
            "get_episodes",
            "get_profile",
            "get_index",
            "get_streams",
            "get_old_streams",
            "get_license",
            "get_manifest"
        ]
    )

    generate_documentation(
        directory="/types",
        base_class="crunpyroll.types",
        auto_type="class",
        template=TYPES_TEMPLATE,
        keys=[
            "SearchQuery",
            "Series",
            "SeasonsQuery",
            "Season",
            "EpisodesQuery",
            "Episode",
            "Movie",
            "Profile",
            "SessionIndex",
            "CMS",
            "MediaStreams",
            "SubtitlesStream",
            "HardsubStream",
            "OldMediaStreams",
            "Manifest",
            "ManifestVideoStream",
            "ManifestAudioStream",
            "ContentProtection",
            "DRM",
            "Image",
            "Images"
        ]
    )
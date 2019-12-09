import os
import amap.config.atlas


def test_get_atlas_pix_sizes(monkeypatch):
    from amap.config.config import get_config_ob
    from amap.tools.source_files import source_custom_config

    cfg_file_path = source_custom_config()
    config_obj = get_config_ob(cfg_file_path)
    monkeypatch.setitem(
        config_obj,
        "atlas",
        {
            "path": os.path.join(
                "..",
                "data",
                "atlas",
                "allen_cff_october_2017_atlas_annotations_10_um.nii",
            )
        },
    )
    atlas = amap.config.atlas.Atlas(cfg_file_path)
    for key, expected_key in zip(
        sorted(atlas.pix_sizes.keys()), ("x", "y", "z")
    ):
        assert key == expected_key
    assert (isinstance(v, float) for v in atlas.pix_sizes.values())

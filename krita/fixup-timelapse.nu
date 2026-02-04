def main [$path: string] {
    let path_obj = $path | path parse
    let out_path = $path_obj.parent | path join $"($path_obj.stem)-clean.($path_obj.extension)"

    # Remove white frames from krita's timelapse. Apparently, there is some
    # bug in Krita that causes it to insert white frames at random intervals:
    # https://krita-artists.org/t/white-flashes-on-time-lapse/87441
    # https://bugs.kde.org/show_bug.cgi?id=476326
    let filter = (
        [
            "negate",
            "blackframe=amount=0:threshold=98",
            "metadata=select:key=lavfi.blackframe.pblack:value=98:function=less",
            "negate",
            "setpts=N/FRAME_RATE/TB"
        ]
        | str join ","
    )

    print --stderr $"Writing to ($out_path). Filter: ($filter)"

    ffmpeg -i $path -vf $filter -an $out_path
}

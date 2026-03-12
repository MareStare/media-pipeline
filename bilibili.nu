def main [] {}

def "main download" [video_url: string] {
    # Download with the best video (bv) and the best audio (ba) quality
    ^yt-dlp.exe -f "bv*+ba/b" $video_url
}

def "main encode" [path: string] {
    let path_obj = $path | path parse
    let out_path = $path_obj.parent | path join $"($path_obj.stem)-encoded.($path_obj.extension)"

    # crf is from 0 to 51 (0 is lossless compression)
    ffmpeg -y -i $path -c:v libx264 -preset veryslow -crf 20 -pix_fmt yuv420p -movflags +faststart $out_path
}

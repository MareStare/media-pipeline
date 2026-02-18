def main [
    --audio: string
    --image: string
    --resolution: string
    --start: string
    --end: string
] {
    mut filters = []

    if $resolution != null {
        $filters = [$"scale=($resolution)"] | append $filters
    }

    if not ($filters | is-empty) {
        $filters = ["-vf" ($filters | str join ",")] | append $filters
    }

    let image_path = $image | path parse

    let output = $image_path.parent | path join $"($image_path.stem)-voiced.mp4"

    mut range = []

    if $start != null {
        $range = ["-ss" $start] | append $range
    }

    if $end != null {
        $range = ["-to" $end] | append $range
    }


    let params = (
        [-y]
        | append $range
        | append [
            -i $audio
            -loop 1
            -i $image
            -map 1:v:0
            -map 0:a:0
        ]
        | append $filters
        | append [
            -tune stillimage
            -c:v libx264
            -pix_fmt yuv420p
            -c:a aac
            -shortest
            $output
        ]
    )

    print --stderr $"> ffmpeg ($params | str join ' ')"

    ffmpeg $params
}

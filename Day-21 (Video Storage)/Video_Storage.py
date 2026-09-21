def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    if video_unit not in ["B", "KB", "MB", "GB"]:
        return "Invalid video unit"
    if drive_unit not in ["GB", "TB"]:
        return "Invalid drive unit"
    if video_unit == "B":
        video_size = video_size/1000/1000/1000
    elif video_unit == "KB":
        video_size = video_size/1000/1000
    elif video_unit == "MB":
        video_size = video_size/1000
    if drive_unit == "TB":
        drive_size = drive_size*1000
    videos = drive_size/video_size
    return int(videos)
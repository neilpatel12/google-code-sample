"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.list_of_played_videos_ids = []
        self.paused_id_list = []
        

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for video in list(self._video_library.get_all_videos()):
            print(video.title)

    def play_video(self, video_id):
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """
        

        if str(video_id) in list(self._video_library.get_all_video_ids()):
            self.list_of_played_videos_ids.append(str(video_id))

            if len(self.list_of_played_videos_ids) == 1:
                self.video_current = VideoLibrary.get_video(self._video_library, self.list_of_played_videos_ids[-1])
                print(f"Playing video: {self.video_current.title}")
            elif len(self.list_of_played_videos_ids) > 1:
                self.video_current = VideoLibrary.get_video(self._video_library, self.list_of_played_videos_ids[-1])
                self.video_previous = VideoLibrary.get_video(self._video_library, self.list_of_played_videos_ids[-2])
                print(f'Stopping video: {self.video_previous.title}')
                print(f"Playing video: {self.video_current.title}")
            else: 
                self.video_current = None
                self.video_previous = None
        else:
            print('Cannot play video: Video does not exist')
            
    def stop_video(self):
        """Stops the current video."""  
        video_current = VideoLibrary.get_video(self._video_library, self.list_of_played_videos_ids[-1])
        print(f"Stopping video: {video_current.title} ")

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_id_random = (random.choice(list(self._video_library.get_all_videos()))).video_id
        self.play_video(video_id_random)

       # print("Playing video: {video_random.title} ")

    def pause_video(self):
        """Pauses the current video."""
        self.paused_id_list.append(str(self.video_current.video_id))
        if len(self.paused_id_list) >= 2:
            print(f'Video already paused: {self.video_current.title}')
            del self.paused_id_list[-1]
        else:   
            print(f"Pausing video: {self.video_current.title}")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.video_current.video_id in self.paused_id_list:
            print(f'Continuing video: {self.video_current.title}')
            del self.paused_id_list[-1]
        else:
            print('Cannot continue video: Video is not paused')

    def show_playing(self):
        """Displays video currently playing."""
        string_tag = " ".join(str(x) for x in self.video_current.tags)
        if len(self._video_library.get_all_videos()) == 0:
            print('No video is currently playing')
        elif self.video_current.video_id in self.paused_id_list:
            print(f"Currently playing: {self.video_current.title} ({self.video_current.video_id}) [{string_tag}] - PAUSED")
        else:
            print(f"Currently playing: {self.video_current.title} ({self.video_current.video_id}) [{string_tag}]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

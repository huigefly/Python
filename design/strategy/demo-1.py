

class config:
    download_tool_type = "bt_bittorrent"

class MainWin:
    def run(self, config):
        print ("main win enter")
        dl = None
        if config.download_tool_type == "bt_bittorrent":
            dl = bittorrent()
            # is block
            thread.start(dl.downloadless(torrent))
        elif config.download_tool_type == "bt_cpp_libtorrent":
            dl = cpp_libtorrent()
            dl.run(torrent)
        elif config.download_tool_type == "bt_python_libtorrent":
            dl = python_libtorrent()
            dl.add_torrent()
            dl.run()
        elif config.download_tool_type == "http_download":
            dl = http_download()
            dl.start()

        # if need, update progress
        while ((progress = download.progress()) != 100){
            progress = 0
            if config.download_tool_type == "bt_bittorrent":
                progress = dl.progress()
            elif config.download_tool_type == "bt_cpp_libtorrent":
                progress = dl.get_progress()
            elif config.download_tool_type == "bt_python_libtorrent":
                progress = dl.progress_value()
            elif config.download_tool_type == "http_download":
                progress = dl.progress()

            if flag == cancel:
                if config.download_tool_type == "bt_bittorrent":
                    dl.stop()
                elif config.download_tool_type == "bt_cpp_libtorrent":
                    dl.cancel()
                elif config.download_tool_type == "bt_python_libtorrent":
                    dl.kill()
                elif config.download_tool_type == "http_download":
                    dl.kill()

            # update
            bar_progress.update(progress)
        }



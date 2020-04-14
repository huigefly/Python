

class config:
    download_tool_type = "bt_bittorrent"

class download:
    def start_bg(self, download_path):
        pass
    
    def progress(self):
        pass
    
    def stop(self):
        pass

class bittorrent(download):
    def start_bg(self, download_path):
        self.dl = bittorrent()
        thread.start(dl.downloadless(download_path))

    def progress(self):
        return self.dl.progress()
    
    def stop(self):
        self.dl.stop()

class cpp_libtorrent(download):
    def start_bg(self, download_path):
        dl = cpp_libtorrent()
        thread.start(dl.run(download_path))

    def progress(self):
        return self.dl.get_progress()
    
    def stop(self):
        self.dl.cancel()

class python_libtorrent(download):
    def start_bg(self, download_path):
        dl = python_libtorrent(download_path)
        dl.add_torrent()
        dl.run()

    def progress(self):
        return self.dl.progress_value()
    
    def stop(self):
        self.dl.kill()

class http_download(download):
    def start_bg(self, download_path):
        dl = http_obj()
        dl.set(download_path)

    def progress(self):
        return self.dl.progress_value()
    
    def stop(self):
        self.dl.stop()

class downloadToolFactory:
    def get(self, tool_type):
        if tool_type == "bt_bittorrent":
            return bittorrent()
        elif tool_type == "cpp_libtorrent":
            return cpp_libtorrent()
        elif tool_type == "python_libtorrent":
            return python_libtorrent()
        elif tool_type == "http_download":
            return http_download()

class MainWin:
    def run(self, config):
        print ("main win enter")
        # data_info: input from other module
        data_info = {download_path:xxx, attr: xxx}
        dl = downloadToolFactory(config.download_tool_type)
        dl.start_bg(data_info.download_path)

        # if need, update progress
        while ((progress = download.progress()) != 100){
            progress = 0
            progress = dl.progress()

            if flag == cancel:
                dl.stop()

            # update
            bar_progress.update(progress)
        }



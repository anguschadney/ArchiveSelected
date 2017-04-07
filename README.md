## ArchiveSelected

Plugin for [fman.io](https://fman.io) to archive files selected in fman (zip and move to a timestamped folder in .old).

[Install](https://fman.io/docs/plugins) by pressing **Ctrl+Shift+p** in fman, selecting "Install plugin", and choosing "ArchiveSelected".

Thanks to [raguay](https://github.com/raguay) whose [code](https://github.com/raguay/ZipSelected) I shamelessly ~~hacked~~, ~~copied~~, extended.

### Usage

Select one or more files / dirs (or just move the cursor over one file / dir), press **F3** and the files / folders will be archived.

The archive directory has the format `./.old/YYYY-mm-DDTHH:MM:SS.zip`

See [here](https://fman.io/docs/custom-shortcuts) to change the key bindings.

### Features

 - Archives selected files

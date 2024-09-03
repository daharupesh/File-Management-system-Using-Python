import os,shutil
# Define the file types and their corresponding extensions and names
file_types = {
    'Images': {
        'Extensions': ['ai', 'bmb', 'gif', 'ico', 'jpeg', 'jpg', 'max', 'obj', 'png', 'ps', 'psd', 'svg', 'tif', 'tiff', '3ds', '3dm'],
        'File Names': ['AI Image(ai)', 'Bitmap Image(bmb)', 'Graphics Interchange Format(gif)', 'Icon File(ico)', 'Joint Photographic Experts Group(jpeg)', 'JPEG Image(jpg)', 'Autodesk 3ds Max Scene(max)', 'Wavefront OBJ File(obj)', 'Portable Network Graphics(png)', 'PostScript(ps)', 'Photoshop Document(psd)', 'Scalable Vector Graphics(svg)', 'Tagged Image File Format(tif)', 'TIFF Image(tiff)', '3D Studio Scene(3ds)', 'Rhino 3D Model(3dm)']
    },
    'Text Files': {
        'Extensions': ['doc', 'docx', 'odt', 'msg', 'pdf', 'rtf', 'tex', 'txt', 'wks', 'wps', 'wpd'],
        'File Names': ['Word Document(doc)', 'Word Document(docx)', 'Open Document Text(odt)', 'Outlook Message(msg)', 'Portable Document Format(pdf)', 'Rich Text Format(rtf)', 'LaTeX Document(tex)', 'Plain Text(txt)', 'Microsoft Works Document(wks)', 'Microsoft Works Document(wps)', 'WordPerfect Document(wpd)']
    },
    'Executable Files': {
        'Extensions': ['apk', 'bat', 'bin', 'cgi', 'com', 'exe', 'jar', 'py', 'wsf', 'ipynb'],
        'File Names': ['Android Package(apk)', 'Batch File(bat)', 'Binary File(bin)', 'Common Gateway Interface Script(cgi)', 'Command File(com)', 'Executable File(exe)', 'Java Archive(jar)', 'Python Script(py)', 'Windows Script File(wsf)', 'Jupyter Notebook(ipynb)']
    },
    'Audio Files': {
        'Extensions': ['aif', 'cda', 'iff', 'mid', 'midi', 'mp3', 'mpa', 'wav', 'wma', '3g2', '3gp'],
        'File Names': ['Audio Interchange File Format(aif)', 'Compact Disc Audio Track(cda)', 'Interchange File Format(iff)', 'MIDI File(mid)', 'MIDI File(midi)', 'MP3 Audio File(mp3)', 'MPEG Audio(mpa)', 'Waveform Audio File Format(wav)', 'Windows Media Audio(wma)', '3GPP2 Multimedia File(3g2)', '3GPP Multimedia File(3gp)']
    },
    'Video Files': { 
        'Extensions': ['mp4', 'avi', 'flv', 'mkv', 'mov', 'wmv'],
        'File Names': ['MPEG-4 Video File(mp4)', 'Audio Video Interleave(avi)', 'Flash Video(flv)', 'Matroska Video File(mkv)', 'Apple QuickTime Movie(mov)', 'Windows Media Video(wmv)']
    },
    'Spreadsheets': {
        'Extensions': ['ods', 'xlr', 'xls', 'xlsx'],
        'File Names': ['OpenDocument Spreadsheet(ods)', 'Microsoft Works Spreadsheet(xlr)', 'Microsoft Excel Spreadsheet(xls)', 'Microsoft Excel Spreadsheet(xlsx)']
    },
    'Presentations': {
        'Extensions': ['key', 'odp', 'pps', 'ppt', 'pptx'],
        'File Names': ['Keynote Presentation(key)', 'OpenDocument Presentation(odp)', 'PowerPoint Slide Show(pps)', 'PowerPoint Presentation(ppt)', 'PowerPoint Presentation(pptx)']
    },
    'Database Files': {
        'Extensions': ['accdb', 'csv', 'dat', 'db', 'dbf', 'log', 'mdb', 'pdb', 'sav', 'sql', 'tar'],
        'File Names': ['Access Database(accdb)', 'Comma-Separated Values(csv)', 'Data File(dat)', 'Database File(db)', 'Database File(dbf)', 'Log File(log)', 'Microsoft Database(mdb)', 'Palm Desktop Database(pdb)', 'SPSS Data File(sav)', 'Structured Query Language(sql)', 'Tape Archive(tar)']
    },
    'Web Files': {
        'Extensions': ['asp', 'aspx', 'cer', 'cfm', 'cgi', 'pl', 'css', 'htm', 'html', 'js', 'part', 'php', 'rss', 'xhtml'],
        'File Names': ['Active Server Pages(asp)', 'Active Server Page Executable(aspx)', 'Security Certificate(cer)', 'ColdFusion Markup Language File(cfm)', 'Common Gateway Interface Script(cgi)', 'Perl Script(pl)', 'Cascading Style Sheet(css)', 'Hypertext Markup Language(htm)', 'Hypertext Markup Language(html)', 'JavaScript File(js)', 'Partially Downloaded File(part)', 'Hypertext Preprocessor(php)', 'Really Simple Syndication(rss)', 'Extensible Hypertext Markup Language(xhtml)']
    },
    'System Files': {
        'Extensions': ['bak', 'cab', 'cfg', 'cpl', 'cur', 'dll', 'dmp', 'drv', 'icns', 'ico', 'ini', 'lnk', 'msi', 'sys', 'tmp'],
        'File Names': ['Backup File(bak)', 'Windows Cabinet File(cab)', 'Configuration File(cfg)', 'Control Panel Extension(cpl)', 'Cursor File(cur)', 'Dynamic Link Library(dll)', 'Dump File(dmp)', 'Device Driver(drv)', 'Icon File(icns)', 'Icon File(ico)', 'Configuration File(ini)', 'Shortcut(lnk)', 'Windows Installer Package(msi)', 'System File(sys)', 'Temporary File(tmp)']
    }
}


def organize_files(folder_path):
    list_of_files = os.listdir(folder_path)
    # print(list_of_files)
    for files in list_of_files:
        extension = files.split('.')[-1].lower()
        # print(extension)
        for key,values in file_types.items():
            if extension in values['Extensions']:
            # Get the index of the extension to find the corresponding files...
                index = values['Extensions'].index(extension)
                # print(index)
                file_name = values['File Names'][index]
                # print(file_name)

                # Create the directory structure
                category_path = os.path.join(folder_path, key)
                specific_path = os.path.join(category_path,file_name)

                if not os.path.exists(specific_path):
                    os.makedirs(specific_path)

                # Move the file to the corresponding directory...
                source = os.path.join(folder_path,files)
                destination = os.path.join(specific_path,files) 
                shutil.move(source,destination)
                break
                # once the file is moved exit the current loop go for next file   

            
# Drive code
folder_path = "C:\\Users\\rupes\\Downloads\\File organization"
organize_files(folder_path)
print("File Organized successfully")
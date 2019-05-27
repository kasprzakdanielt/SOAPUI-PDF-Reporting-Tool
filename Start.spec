block_cipher = None
import shutil
shutil.copyfile('config.cfg', '{0}/config.cfg'.format(DISTPATH))
#shutil.copyfile(Tree('Html_files', prefix='Html_files'), '{0}/{}'.format(DISTPATH, Tree('Html_files', prefix='Html_files')))
import pyphen
pyphen_root = os.path.dirname(pyphen.__file__)
pyphen_dictionaries = Tree(os.path.join(pyphen_root, 'dictionaries'), prefix = 'pyphen/dictionaries')

a = Analysis(['Start.py'],
             
			 pathex=['C:\\Users\\Daniel\\Desktop\\release tool\\SOAPUIReportingTool\\soap'],
             binaries=[],
             datas=[
                 ("C:\\Program Files\\Python37\\Lib\\site-packages\\tinycss2\\VERSION", "tinycss2"),
                 ("C:\\Program Files\\Python37\\Lib\\site-packages\\cairocffi\\VERSION", "cairocffi"),
                 ("C:\\Program Files\\Python37\\Lib\\site-packages\\\weasyprint\\VERSION", "."),
				 ("C:\\Program Files\\Python37\\Lib\\site-packages\\weasyprint\\css\\html5_ua.css", "css"),
				 ("C:\\Program Files\\Python37\\Lib\\site-packages\\weasyprint\\css\\html5_ph.css", "css")
                     ],
             hiddenimports=["tinycss2", "matplotlib", "weasyprint"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
		  pyphen_dictionaries,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True )
		  

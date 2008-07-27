Name: 	 	lplayer
Summary: 	Music collection manager and player
Version: 	1.0
Release: 	%mkrel 3
License:	GPLv2+
Group:		Sound
URL:		http://lplayer.sourceforge.net/
Source:		http://nchc.dl.sourceforge.net/sourceforge/lplayer/%{name}_%{version}.tar.gz
Source1:	lplayer.png
Patch0:		lplayer-db4_headers_fix.diff
BuildRequires:	xmms-devel qt3-devel ImageMagick
BuildRequires:	db4-devel
Requires:	xmms
Provides:	longplayer
Obsoletes:	longplayer
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LongPlayer is a program that automatically fills your XMMS.  LongPlayer tries
maximize the timespan between you hearing the same song twice.
    * make random, playlists in a matter of seconds: dynamic collections of
      directories you want to hear (no need to add newly downloaded music)
    * rate your songs and assign a color/genre
    * always hear the music you want to hear, based on:
          o the last time you heard it
          o the rating and genre 

%prep

%setup -q -n %name
%patch0 -p0

%build
rm -f configure
autoreconf -fis

%configure2_5x
make

%install
rm -rf %{buildroot}

%makeinstall

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=LongPlayer
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;
Encoding=UTF-8
EOF

#icons
# ImageMagick didn't like included icon
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 %SOURCE1 %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 %SOURCE1 %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 %SOURCE1 %{buildroot}/%_miconsdir/%name.png

%find_lang %name

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS FAQ README TODO
%{_bindir}/%name
%{_datadir}/lplayer
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

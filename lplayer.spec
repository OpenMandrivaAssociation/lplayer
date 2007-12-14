%define name	lplayer
%define version	1.0
%define release %mkrel 1


Name: 	 	%{name}
Summary: 	Music collection manager and player
Version: 	%{version}
Release: 	%{release}

Source:		http://nchc.dl.sourceforge.net/sourceforge/lplayer/%{name}_%{version}.tar.gz
Source1:	lplayer.png
URL:		http://lplayer.sourceforge.net/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	xmms-devel qt3-devel ImageMagick
Requires:	xmms
Provides:	longplayer
Obsoletes:	longplayer

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

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="LongPlayer" longtitle="Playlist manager" section="Multimedia/Sound" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %SOURCE1 $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %SOURCE1 $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %SOURCE1 $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS FAQ README TODO
%{_bindir}/%name
%{_datadir}/lplayer
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


Summary:	The Blue Mago Quest - pacman style 3D game
Summary(pl):	The Blue Mago Quest - gra 3D w stylu pacman
Name:		mangoquest
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	mangopeeler.desktop
Patch0:		%{name}-CFLAGS.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-nodoc.patch
URL:		http://%{name}.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
The Blue Mango Quest is a 3D arcade game that uses OpenGL and SDL. The goal is
to extend the pacman-style gameplay in several ways. You see what the main
character sees (like in traditional FPS games), and you'll find about 20 items
(bonus and malus) that will give you a lot of fun. An easy to use yet powerfull
2D level editor is also provided.


%description -l pl
The Blue Mango Quest to trójwymiarowa gra zrêczno¶ciowa wyko¿ystuj±ca OpenGL 
i SDL. Jej celem jest wielostronne rozszerzenie gry w stylu pacman'a. Widzisz
to co widzi g³ówny bochater (jak w tradycyjnych grach FPS), i mo¿esz znale¼æ
oko³o 20 przedmiotów (bonusów itp.) które sprawi± du¿o frajdy. Dostêpny jest
tak¿e edytor poziomów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
automake
autoconf
%configure \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib" \
	CPPFLAGS="-I%{_includedir}" 

%{__make} 

bunzip2 -c doc/manuals.tar.bz2 | tar xf - -C doc/
mv doc/home/phneutre/Developpement/ShmiX/Web/sourceforge/doc doc/manuals
chmod -R a-x,a+rX doc/manuals

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/mangopeeler.desktop

mv mangopeeler/ChangeLog ChangeLog-mangopeeler
gzip -9nf README NEWS TODO AUTHORS ChangeLog ChangeLog-mangopeeler

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/manuals doc/*.fig.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mangoquest
%{_datadir}/mangopeeler
%{_applnkdir}/Games/*

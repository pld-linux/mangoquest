Summary:	The Blue Mago Quest - pacman style 3D game
Summary(pl.UTF-8):	The Blue Mago Quest - gra 3D w stylu pacman
Name:		mangoquest
Version:	0.6.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/mangoquest/%{name}-%{version}.tar.bz2
# Source0-md5:	2433d792151bd87baacb33935b1e94d1
Source1:	%{name}.desktop
Source2:	mangopeeler.desktop
Source3:	%{name}.png
URL:		http://mangoquest.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Blue Mango Quest is a 3D arcade game that uses OpenGL and SDL. The
goal is to extend the pacman-style gameplay in several ways. You see
what the main character sees (like in traditional FPS games), and
you'll find about 20 items (bonus and malus) that will give you a lot
of fun. An easy to use yet powerfull 2D level editor is also provided.

%description -l pl.UTF-8
The Blue Mango Quest to trójwymiarowa gra zręcznościowa wykorzystująca
OpenGL i SDL. Jej celem jest wielostronne rozszerzenie gry w stylu
pacmana. Widzisz to co widzi główny bohater (jak w tradycyjnych grach
FPS), i możesz znaleźć około 20 przedmiotów (bonusów itp.) które
sprawią dużo frajdy. Dostępny jest także edytor poziomów.

%prep
%setup -q

%build
rm -f missing acinclude.m4
%{__aclocal}
%{__autoconf}
%{__automake}

cd mangopeeler
rm -f missing acinclude.m4
%{__aclocal}
%{__autoconf}
%{__automake}
cd -

%configure  \
 	LDFLAGS="-L%{_libdir}" \
	CPPFLAGS="-I%{_includedir}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/mangopeeler.desktop
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -rf %{_datadir}/%{name}/doc

mv -f mangopeeler/ChangeLog ChangeLog-mangopeeler

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO AUTHORS ChangeLog ChangeLog-mangopeeler doc/manuals
%attr(755,root,root) %{_bindir}/*
%{_mandir}goquest
%{_mandir}gopeeler
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

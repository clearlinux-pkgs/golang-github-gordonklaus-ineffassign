Name     : golang-github-gordonklaus-ineffassign
Version  : 71e35c2a79cb470e72313ec93d6750089dc95fa3
Release  : 2
URL      : https://github.com/gordonklaus/ineffassign/archive/71e35c2a79cb470e72313ec93d6750089dc95fa3.tar.gz
Source0  : https://github.com/gordonklaus/ineffassign/archive/71e35c2a79cb470e72313ec93d6750089dc95fa3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go

%description
# ineffassign
Detect ineffectual assignments in Go code.

%prep
%setup -q -n ineffassign-71e35c2a79cb470e72313ec93d6750089dc95fa3

%build
export LANG=C

%install
gopath="/usr/lib/golang"
library_path="github.com/gordonklaus/ineffassign"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/gordonklaus/ineffassign/ineffassign.go

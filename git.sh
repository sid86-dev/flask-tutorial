clear
# optional color variables
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`
echo "${red}remote: -----> ${green}Tracking all files...${reset}";
echo -en '\n';
git add .;
echo -en '\n';
echo "${red}remote: -----> ${green}moving all files to commit...${reset}";
echo -en '\n';
echo "${green}Enter the push reason: ${reset}";
read push_type
git commit -m "$push_type";
echo -en '\n';
echo "${red}remote: -----> ${green}pushing all files to branch...${reset}";
echo -en '\n';
git push all master;
echo -en '\n';
echo "${red}remote: -----> ${green}git push success...${reset}";
echo -en '\n';
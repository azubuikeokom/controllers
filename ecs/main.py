from git_repo import Repo

git_repo = Repo("https://github.com/azubuikeokom/java-basics.git")
git_repo.clone(branch="main")
#get latest ecr image digest
#compare with local image digest
#if different update terraform files with new image digest
#push changes to git
#merge PR to main branch
#run terraform plan
#run terraform apply
#deploy new image to ECS
#update channel with deployment status
#notify user of deployment status
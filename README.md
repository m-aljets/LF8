# LF8

## Improvements

### Seperate jobs in workflow

Everything was done within one job before. Now there are four different jobs:

- build
- lint
- test
- deploy

### Deploy stage in workflow

We don't have our script running on a server, so we don't have a productive environment to deploy to. For this reason, to be able to have a deploy stage nevertheless, we created a "deploy-env" 	environment in GitHub that we deploy our code to. In addition we define and use an environment variable in this stage. 


### Pipeline quality measures

- linter
- workflow is triggered schedueled (workflow runs every morning at 8am) and manually in addition to only being run if a developer pushes to the repo
- "needs" attribute in jobs: one job can only start if needed jobs are successfully finished
	- test and lint job are only started when build job is successful
	- deployment only starts when test and lint jobs are successful
	
	
### Class and sequence diagrams

Class diagram: https://drive.google.com/file/d/19I55txKxGC7Cm3VqY7afn4dk5Nl-HSWJ/view?usp=sharing

Sequence diagram: https://drive.google.com/file/d/1vv3gI6J46ldkY-Avwdzxz5BvxKFQMAKm/view?usp=sharing


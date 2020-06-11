## Tags

Get tags and prune the local ones
```
git fetch origin --prune --prune-tags
```

## Lost stuff

Get all 'dangling' commits, which means all commits that are never used but still in the reflog. E.g. stashes that have been deleted accidentially.

```
git log --graph --oneline --decorate ( git fsck --no-reflog | awk '/dangling commit/ {print $3}' )

https://stackoverflow.com/questions/89332/how-to-recover-a-dropped-stash-in-git/91795#91795
```

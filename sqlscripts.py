# sqlscripts.py - Contains the sql scripts for ACDS deployment checks.

# SQL script to get the deployed projects
project_sql = """
SELECT 
	p.Project,
	p.DeployedBy,
	p.DeployedTime,
	f.name AS Folder
FROM
	(
		SELECT
			pr.name AS Project, 
			ov.object_version_lsn,
			ov.created_by AS DeployedBy, 
			pr.folder_id,
			CONVERT(varchar(10), ov.created_time, 121) + ' ' + CONVERT(varchar(5), ov.created_time, 108) AS DeployedTime,
			ROW_NUMBER() OVER(PARTITION BY pr.name ORDER BY ov.object_version_lsn DESC) AS Num
		FROM 
			internal.object_versions ov
		LEFT JOIN
				internal.projects pr ON ov.[object_id] = pr.project_id
	) p
INNER JOIN
	internal.folders f ON p.folder_id = f.folder_id
WHERE
	p.Num = 1
    """

package_sql = """
WITH Latests AS
(
	SELECT 
		p.Project,
		p.DeployedBy,
		p.DeployedTime,
		p.Versions
	FROM
		(
			SELECT
				pr.name AS Project, 
				ov.object_version_lsn AS Versions,
				ov.created_by AS DeployedBy, 
				CONVERT(varchar(10), ov.created_time, 121) + ' ' + CONVERT(varchar(5), ov.created_time, 108) AS DeployedTime,
				ROW_NUMBER() OVER(PARTITION BY pr.name ORDER BY ov.object_version_lsn DESC) AS Num
			FROM 
				internal.object_versions ov
			LEFT JOIN
					internal.projects pr ON ov.[object_id] = pr.project_id
		) p
	WHERE
		p.Num = 1
)

SELECT
    l.Project,
    REPLACE(pa.name,'.dtsx','') AS Package,
    CAST(pa.version_build AS VARCHAR(10)) AS DeployedVersion
FROM 
	internal.packages pa
INNER JOIN
	Latests l ON pa.project_version_lsn = l.Versions
ORDER BY
	l.Project,
	pa.name
    """


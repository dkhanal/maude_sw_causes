CREATE VIEW [dbo].[VW_FOI_TEXT_LABELED_DATA]
AS
SELECT 'pos' AS LABEL, * FROM [dbo].[FOI_TEXT_LABELED_DATA_POSITIVE]
UNION
SELECT 'neg' AS LABEL, * FROM [dbo].[FOI_TEXT_LABELED_DATA_NEGATIVE]
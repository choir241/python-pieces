const doc = `
---
title: My title
---

# {% $frontmatter.title %} 
`;

const ast = Markdoc.parse(doc);

# MyST Test File

This file tests MyST Markdown features on GitHub.

## Standard Markdown (should work)

**Bold**, *italic*, `code`

- List item 1
- List item 2

## MyST-Specific Features (likely won't render)

### Admonition Directive

```{note}
This is a note admonition.
```

```{warning}
This is a warning!
```

:::{tip}
This is a tip using colon fence.
:::

### Roles

This is a {term}`glossary term`.

See {ref}`some-label` for more info.

### Math

Inline math: $E = mc^2$

Block math:
$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$

### Definition List

Term 1
: Definition of term 1

Term 2
: Definition of term 2

### Task List (GFM - should work)

- [x] Completed task
- [ ] Incomplete task

## Conclusion

If you see raw `{note}`, `{warning}`, `:::` syntax above, MyST is NOT rendering on GitHub.
